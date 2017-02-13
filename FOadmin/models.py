from django.db import models
from django.contrib.auth.models import User

#Профиль пользователя
class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete = models.CASCADE,
                                primary_key=True)
    fo_user_last_name = models.CharField(max_length=50, verbose_name='Фамилия', default="-")
    fo_user_name = models.CharField(max_length=50, verbose_name='Имя', default="-")
    fo_user_patronymic = models.CharField(max_length=50, verbose_name='Отчество', default="-")
    fo_user_birthday = models.DateField(default="1900-01-01", verbose_name='День рождения')

    class Meta:
        verbose_name = 'Информацию о пользователе'
        verbose_name_plural = 'Информация о пользователях'
        ordering = ['fo_user_last_name']

