from django.contrib import admin
from FoCounterparty.models import LegalEntity



class LegalEntityAdmin(admin.ModelAdmin):
    pass



admin.site.register(LegalEntity, LegalEntityAdmin)