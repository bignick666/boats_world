from django.contrib import admin
from .models import Group, OutboardMotor


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class OutboardMotorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model', 'type', 'max_power', 'weight', 'group')
    search_fields = ('model', 'type', 'max_power', 'group')
    list_filter = ('model', 'type', 'max_power')


admin.site.register(Group, GroupAdmin)
admin.site.register(OutboardMotor, OutboardMotorAdmin)
