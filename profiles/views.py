from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

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

