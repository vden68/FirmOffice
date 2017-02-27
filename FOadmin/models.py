from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
import mptt

#Профиль пользователя
def fo_user_upload_path(instance, filename):
    return 'profile/fo_user/{0}/{1}'.format(instance.user, filename)

class Profile(models.Model):

    WORKPHONE = 'WP'
    PRIVATEPHONE = 'PP'
    CELLULARPHONE = 'CP'
    INTEROFFICETELEPHONE = 'IP'
    PHONE_TYPE = (
        (WORKPHONE, 'Рабочий телефон'),
        (PRIVATEPHONE, 'Личный телефон'),
        (CELLULARPHONE, 'Сотовый телефон'),
        (INTEROFFICETELEPHONE, 'Внутренний телефон'),
    )

    user = models.OneToOneField(User,
                                on_delete = models.CASCADE,
                                primary_key=True)
    fo_user_last_name = models.CharField(max_length=50, verbose_name='Фамилия', default="-")
    fo_user_name = models.CharField(max_length=50, verbose_name='Имя', default="-")
    fo_user_patronymic = models.CharField(max_length=50, verbose_name='Отчество', default="-")
    fo_user_birthday = models.DateField(default="1900-01-01", verbose_name='День рождения')
    fo_user_email = models.EmailField(default='test@test.ru', verbose_name='Email')
    fo_user_type_phone_1 = models.CharField(max_length=2, choices=PHONE_TYPE, default=WORKPHONE, verbose_name='Тип телефона')
    fo_user_phone_1 = models.CharField(max_length=20, default='-', verbose_name='№ телефона')
    fo_user_type_phone_2 = models.CharField(max_length=2, choices=PHONE_TYPE, default=WORKPHONE, verbose_name='Тип телефона')
    fo_user_phone_2 = models.CharField(max_length=20, default='-', verbose_name='№ телефона')
    fo_user_type_phone_3 = models.CharField(max_length=2, choices=PHONE_TYPE, default=WORKPHONE, verbose_name='Тип телефона')
    fo_user_phone_3 = models.CharField(max_length=20, default='-', verbose_name='№ телефона')
    fo_user_type_phone_4 = models.CharField(max_length=2, choices=PHONE_TYPE, default=WORKPHONE, verbose_name='Тип телефона')
    fo_user_phone_4 = models.CharField(max_length=20, default='-', verbose_name='№ телефона')
    fo_user_photo = models.ImageField(upload_to=fo_user_upload_path, blank=True, verbose_name='Фото пользователя')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        ordering = ['fo_user_last_name']

class CompanyStructure(MPTTModel):
    title = models.CharField('Название',max_length=100, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __unicode__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Структура компании'
        verbose_name_plural = 'Структура компании'

mptt.register(CompanyStructure)

class TestMptt(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование')
    def __unicode__(self):
        return self.name


