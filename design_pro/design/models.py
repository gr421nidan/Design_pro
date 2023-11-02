from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default='something')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name='Время создания заявки', auto_now_add=True)
    status = models.CharField(max_length=254, default='Новая')
    image = models.ImageField(upload_to="media/", verbose_name="Фотография",
                              help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), validate_image])

    def __str__(self):
        return self.name
