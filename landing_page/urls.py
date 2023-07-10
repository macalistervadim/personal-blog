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
    # Добавление новой записи
    path('topics/add_topic/', views.AddPosts.as_view(), name='add_post'),
    # Редактирование текущей записи
    path('topics/<int:pk>/edit/', views.EditPost.as_view(), name='edit_post'),
    # Удаление текущей записи
    path('topics/<int:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
    # Подтверждение удаления
    path('topics/<int:pk>/delete/confirm/', views.DeletePostConfirm.as_view(), name='delete_post_confirm'),
]