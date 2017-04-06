from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import mptt
import uuid

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

    def __str__(self):
        return '%s %s. %s.' % (self.fo_user_last_name.title(), self.fo_user_name.upper()[0],
                               self.fo_user_patronymic.upper()[0])


#Структура компании
class CompanyStructure(MPTTModel):
    title = models.CharField('Название',max_length=100, unique=True, default=uuid.uuid4)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            verbose_name='Кому подчиняется')
    fo_department = models.ForeignKey('Department', on_delete=models.ProtectedError,
                                      verbose_name='Отдел', null=True, blank=True )
    fo_book_position = models.ForeignKey('ReferenceBookPosition', on_delete=models.ProtectedError,
                                         verbose_name='Должность', null=True, blank=True )
    fo_profile = models.ForeignKey('Profile', on_delete=models.ProtectedError,
                                   verbose_name='ФИО', null=True, blank=True )

    @property
    def title_for_admin(self):
        return "%s %s %s" % (self.fo_department, self.fo_book_position, self.fo_profile)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Структура компании'
        verbose_name_plural = 'Структура компании'

    def __str__(self):
        return  '%s %s %s' % (self.fo_department, self.fo_book_position, self.fo_profile)


mptt.register(CompanyStructure)


#Справочник должностей
class ReferenceBookPosition(models.Model):
    fo_position_name = models.CharField('Должность',max_length=100, unique=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Справочник должностей'

    def __str__(self):
        return '%s' % (self.fo_position_name)


#Справочник отделов
class Department(models.Model):
    fo_department_name = models.CharField('Отдел', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Справочник отделов'

    def __str__(self):
        return '%s' % (self.fo_department_name)




