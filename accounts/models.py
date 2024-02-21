from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    username = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name='Почтовый адрес', unique=True)
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USER_TYPE_CHOICES = [
        ('owner', 'Франчайзер'),
        ('franchise', 'Франчизи'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, verbose_name="Тип пользователя", null=True,
                                 blank=True)

    def __str__(self):
        return self.username
