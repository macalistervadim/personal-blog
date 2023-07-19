from datetime import datetime
from django.db import models
from django.contrib.messages.views import SuccessMessageMixin

def default_datetime(): return datetime.now()

class AddNewPost(models.Model, SuccessMessageMixin):
    """Добавление новой публикации"""
    title = models.CharField('Название записи', max_length=200)
    description = models.TextField('Описание записи')
    date_created = models.DateTimeField('Дата публикации', default=default_datetime())
    image = models.ImageField('Изображение', upload_to='image/%Y', blank=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.date_created}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class AddComment(models.Model):
    """Добавление комментария под определенную запись"""
    email = models.EmailField('Почтовый адрес')
    text = models.TextField('Текст комментария', max_length=250)
    name = models.CharField('Имя', max_length=100)
    post = models.ForeignKey(AddNewPost, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'