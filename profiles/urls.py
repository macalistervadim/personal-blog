# Маршруты для приложения Profiles
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    # Страница входа на сайт
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # Страница выхода с сайта
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # Страница для смены пароля
    path('change_password/', views.ChangePassView.as_view(), name='change_password'),
    # Страница с успешной сменой пароля
    path('change_password/done/', views.PasswordChangeDoneView.as_view(),
                                                        name='change_pass_done'),
    # Страница регистрации
    path('signup/', views.SignUpView.as_view(), name='signup'),
]