from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.urls import reverse

from .models import AddNewPost, AddComment
from .forms import CommentForm, AddPost

class HomePage(View):
    """Домашняя страница"""
    def get(self, request):
        return render(request, 'home.html')

class PostView(View):
    """Вывод записей на страницу"""
    def get(self, request):
        posts = AddNewPost.objects.all().order_by('-date_created')
        paginator = Paginator(posts, 10)  # Пагинация по 10 записей на странице
        page_number = request.GET.get('page')  # Получение номера текущей страницы
        page = paginator.get_page(page_number)  # Получение объекта страницы
        return render(request, 'posts.html', {'page': page})

class PostDetail(View):
    """Страница определенной записи по id"""
    def get(self, request, pk):
        post = AddNewPost.objects.get(id=pk)
        comments = AddComment.objects.filter(post=post)
        return render(request, 'post_detail.html', {'post': post, 'comments': comments})

class AddNewComment(View):
    """Добавление нового комментария к записи"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(reverse('landing_page:post_detail', args=[pk]))


class AddPosts(View):
    """Добавление новой записи на страницу"""

    def get(self, request):
        return render(request, 'add_post.html')

    def post(self, request):
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page:post_list')
        return render(request, 'add_post.html')

class EditPost(View):
    """Редактирование текущей записи"""
    def get(self, request, pk):
        post = AddNewPost.objects.get(id=pk)
        form = AddPost(instance=post)
        return render(request, 'edit_post.html', {'form': form, 'post': post})

    def post(self, request, pk):
        post = AddNewPost.objects.get(id=pk)
        form = AddPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('landing_page:post_detail', pk=pk)
        return render(request, 'edit_post.html', {'form': form, 'post': post})
