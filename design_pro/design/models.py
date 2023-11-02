from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Application(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название заявки', blank=False)
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=False)
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    photo_file = models.ImageField(max_length=254, upload_to='images', blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp'])])
    user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Время создания заявки', auto_now_add=True)
    status = models.CharField(max_length=254, default='Новая')

    def __str__(self):
        return f'{self.name} ({self.date})'


