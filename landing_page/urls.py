# Маршруты для приложения landing_page

from django.urls import path

from . import views

app_name = 'landing_page'
urlpatterns = [
    # Главная страница
    path('', views.PostView.as_view(), name='landing'),
    # Страница конкретной записи
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]