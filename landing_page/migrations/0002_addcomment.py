# Generated by Django 4.2.3 on 2023-07-08 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почтовый адрес')),
                ('text', models.CharField(max_length=250, verbose_name='Текст комментария')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_page.addnewpost', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]