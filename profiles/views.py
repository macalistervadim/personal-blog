from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic.base import View
from django.core.mail import send_mail

from .forms import SignUpForm
from personal_blog import settings

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
            login(request, user, backend=settings.EMAIL_BACKEND[0])

            # Отправка приветственного письма
            subject = 'Добро пожаловать на наш сайт'
            message = 'Добро пожаловать! Спасибо за регистрацию на нашем сайте.'
            from_email = 'noreply@example.com'
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])

            return redirect('landing_page:landing')
        return render(request, 'registration/signup.html', {'form': form})

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

