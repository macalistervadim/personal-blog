from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import AddNewPost

class PostView(View):
    """Вывод записей на страницу"""
    def get(self, request):
        posts = AddNewPost.objects.all()
        return render(request, 'posts.html', {'posts': posts})

class PostDetail(View):
    """Страница определенной записи по id"""
    def get(self, request, pk):
        post = AddNewPost.objects.get(id=pk)
        return render(request, 'post_detail.html', {'post_detail': post})
