from django.db import models

class AddNewPost(models.Model):
    """Добавление новой публикации"""
    title = models.CharField('Название записи', max_length=200)
    description = models.TextField('Описание записи')
    date_created = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.date_created}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'