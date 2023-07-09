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
        return render(request, 'posts.html', {'posts': posts})

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
