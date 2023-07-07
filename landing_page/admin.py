from _ast import Add

from django.contrib import admin

from .models import AddNewPost

@admin.register(AddNewPost)
class AddNewPost(admin.ModelAdmin):
    list_display = ('title', 'date_created')

