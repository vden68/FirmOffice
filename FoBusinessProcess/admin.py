from django.contrib import admin

from FoBusinessProcess.models import BusinessProcess, LineOfBusiness


class BusinessProcessAdmin(admin.ModelAdmin):
    pass

class LineOfBusinessAdmin(admin.ModelAdmin):
    pass



admin.site.register(BusinessProcess, BusinessProcessAdmin)
admin.site.register(LineOfBusiness, LineOfBusinessAdmin)