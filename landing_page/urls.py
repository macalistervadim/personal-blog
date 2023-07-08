# Маршруты для приложения landing_page

from django.urls import path

from . import views

app_name = 'landing_page'
urlpatterns = [
    # Главная страница
    path('', views.HomePage.as_view(), name='landing'),
    # Старница со всеми записями
    path('topics/', views.PostView.as_view(), name='post_list'),
    # Страница конкретной записи
    path('topics/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # Добавление нового комментария
    path('topics/<int:pk>/add_comment/', views.AddNewComment.as_view(), name='add_comment'),
]