from django.db import models
from FOadmin.models import Profile, CompanyStructure
from FoCounterparty.models import LegalEntity


#Бизнес процесс
class BusinessProcess(models.Model):
    fo_business_process_name= models.CharField('Название',max_length=100)
    fo_line_of_business= models.ForeignKey('LineOfBusiness', on_delete=models.ProtectedError,
                                           verbose_name='Отрасль производства(линия бизнеса)')
    fo_business_process_manager= models.ForeignKey(CompanyStructure, on_delete=models.ProtectedError,
                                                   verbose_name='Руководитель Бизнесс процесса')
    #fo_client_person= models.ForeignKey(Profile, on_delete=models.ProtectedError,
    #                                    null=True, blank=True, verbose_name='Заказчик физическое лицо')
    #fo_client_legal_entity= models.ForeignKey(LegalEntity, on_delete=models.ProtectedError,
    #                                          null=True, blank=True, verbose_name='Заказчик Юридическое лицо')
    #fo_date_of_creation= models.DateField(auto_now_add=True, verbose_name='Дата создания бизнес процесса')
    #fo_who_created= models.ForeignKey(Profile, on_delete=models.ProtectedError, verbose_name='Кто создал')
    #fo_automatic_closing= models.BooleanField(default=True, verbose_name='Автоматически при окончании последнего '
    #                                                                     'этапа закрывать проект')


    class Meta:
        verbose_name = 'Бизнес процесс'
        verbose_name_plural = 'Бизнес процессы'

    def __str__(self):
        return '%s' % (self.fo_business_process_name)


#Отрасль производства (линия бизнеса) справочник
class LineOfBusiness(models.Model):
    fo_line_of_business_name=  models.CharField('Отрасль производства',max_length=100)

    class Meta:
        verbose_name = 'Отрасль производства (линия бизнеса)'
        verbose_name_plural = 'Отрасль производства (линия бизнеса)'

    def __str__(self):
        return '%s' % (self.fo_line_of_business_name)
