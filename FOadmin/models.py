from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Доп. информайия')
    fo_patronymic = models.CharField(max_length=50, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'

