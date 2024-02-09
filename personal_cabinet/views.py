from django.shortcuts import render

from .forms import CurrentUserForm


def my_view(request):
    current_user_form = CurrentUserForm(request=request)
    return render(request, 'my_template.html', {'current_user_form': current_user_form})