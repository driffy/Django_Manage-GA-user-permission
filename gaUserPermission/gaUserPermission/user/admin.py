from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import T_Profile

class T_ProfileInline(admin.StackedInline):
    model = T_Profile
    can_delete = False
    verbose_name_plural = 'T_Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (T_ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
