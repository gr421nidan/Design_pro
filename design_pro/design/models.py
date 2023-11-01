# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
#
# class User(AbstractUser):
#     name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
#     surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
#     patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
#     username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
#     email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
#     password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
#
#     def full_name(self):
#         # return self.name + ' ' + self.surname + ' ' + self.patronymic
#         return ' '.join([self.name, self.surname, self.patronymic])
#
#     def __str__(self):
#         return self.full_name()
#
