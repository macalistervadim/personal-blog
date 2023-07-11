# Маршруты для приложения Profiles

from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    # Страница входа на сайт
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # Страница выхода с сайта
    path('logout/', views.CustomLogoutView.as_view(), name='logout')
]