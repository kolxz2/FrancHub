from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegistrationForm, EmailAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Сначала создаем пользователя, но не сохраняем его в базе данных
            password = form.cleaned_data['password']  # Получаем пароль из формы
            user.set_password(password)  # Устанавливаем зашифрованный пароль
            user.save()  # Сохраняем пользователя в базе данных

            # Авторизуем пользователя
            authenticated_user = authenticate(username=user.username, password=password)
            login(request, authenticated_user)

            # После успешной регистрации перенаправляем пользователя на страницу приветствия
            return redirect('greeting')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    # После выхода из системы перенаправляем пользователя на страницу входа или на другую страницу
    return redirect('login_view')


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
        return reverse_lazy('greeting')
