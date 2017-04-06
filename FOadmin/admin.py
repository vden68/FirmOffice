from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from FOadmin.models import Profile,CompanyStructure, ReferenceBookPosition, Department, WorkingGroup


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','fo_user_last_name', 'fo_user_name', 'fo_user_patronymic', 'fo_user_birthday')

    fieldsets = [
        #(None, {'fields': [('user')]}),
        ('ФИО', {'fields': [('fo_user_last_name', 'fo_user_name', 'fo_user_patronymic', 'fo_user_birthday')]}),
        ('Контактные данные', {'fields': ['fo_user_email', ('fo_user_type_phone_1', 'fo_user_phone_1'),
                                          ('fo_user_type_phone_2', 'fo_user_phone_2'),
                                          ('fo_user_type_phone_3', 'fo_user_phone_3'),
                                          ('fo_user_type_phone_4', 'fo_user_phone_4')
                                            ,'fo_user_photo'
                                          ]}),

    ]



class CompanyStructureDjangoMpttAdmin(DjangoMpttAdmin):
    list_display = ('fo_department', 'fo_book_position',)
    item_label_field_name = 'title_for_admin'
    exclude = ('title',)


class ReferenceBookPositionAdmin(admin.ModelAdmin):
    list_display = ('fo_position_name',)


class DepartmentAdmin(admin.ModelAdmin):
    pass

class WorkingGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
#admin.site.register(CompanyStructure, CompanyStructureAdmin)
admin.site.register(ReferenceBookPosition, ReferenceBookPositionAdmin)
admin.site.register(CompanyStructure, CompanyStructureDjangoMpttAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(WorkingGroup, WorkingGroupAdmin)