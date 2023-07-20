from rest_framework import serializers

from .models import AddNewPost

class ViewsPostApi(serializers.ModelSerializer):
    """Сериализатор для вывода постов"""
    class Meta:
        model = AddNewPost
        fields = ('id', 'title')