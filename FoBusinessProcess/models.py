from django.db import models


#Бизнес процесс
class BusinessProcess(models.Model):
    fo_business_process_name= models.CharField('Название',max_length=100)
    fo_line_of_business= models.ForeignKey('LineOfBusiness', on_delete=models.ProtectedError,
                                           verbose_name='Отрасль производства')


#Отрасль производства (линия бизнеса) справочник
class LineOfBusiness(models.Model):
    fo_line_of_business_name=  models.CharField('Отрасль производства',max_length=100)