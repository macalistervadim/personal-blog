from _ast import Add

from django.contrib import admin

from .models import AddNewPost, AddComment

@admin.register(AddNewPost)
class AddNewPost(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(AddComment)
class AddComment(admin.ModelAdmin):
    list_display = ('name', 'text')


