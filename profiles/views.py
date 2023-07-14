from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,\
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic.base import View

from .forms import SignUpForm

class CustomLoginView(LoginView):
    """Шаблон представления формы входа на сайт"""
    template_name = 'registration/login.html'
    next_page = 'landing_page:landing'

class CustomLogoutView(LogoutView):
    """Шаблон представления формы выхода с сайта"""
    next_page = 'landing_page:landing'

class ChangePassView(PasswordChangeView):
    """Шаблон представления смены пароля"""
    template_name = 'registration/password_change_form.html'
    success_url = '/profiles/change_password/done/'

class ChangePassDone(PasswordChangeDoneView):
    """Шаблон представления уведомления об успешной смене пароля"""
    pass

class SignUpView(View):
    """Шаблон представления регистрации на сайте"""
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page:landing')
        return render(request, 'registration/signup.html', {'form': form})
