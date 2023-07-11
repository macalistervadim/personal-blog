from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    next_page = 'landing_page:landing'

class CustomLogoutView(LogoutView):
    template_name = 'registration/login.html'
    next_page = 'landing_page:landing'

