from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(request, email=user.email, password=password)
            login(request, user)
            return redirect('main_list')
    else:
        logout(request)
        form = RegistrationForm()
    return render(request, 'register_page.htm', {'form': form})


def logout_view(request):
    logout(request)
    # После выхода из системы перенаправляем пользователя на страницу входа или на другую страницу
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:

            login(request, user)
            # Получаем предыдущий URL из заголовков запроса
            previous_url = request.META.get('HTTP_REFERER')
            # Если предыдущий URL существует и он не является URL для входа, перенаправляем на него
            if previous_url and previous_url != request.build_absolute_uri(reverse('login')):
                return redirect(previous_url)
            elif user.is_staff or user.is_superuser:
                return redirect('all_site_franchises')
            else:
                return redirect('main_list')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login_page.htm')


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = 'Успешная авторизация'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def form_invalid(self, form):
        messages.error(self.request, ('Ошибка аутентификации'))
        return super().form_invalid(form)

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('main_list')
