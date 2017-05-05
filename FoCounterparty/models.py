from django.db import models

#Юридическое лицо
class LegalEntity(models.Model):
    fo_short_title=  models.CharField('Краткое наименование',max_length=100)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return '%s' % (self.fo_short_title)



