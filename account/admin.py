from django.contrib import admin

from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'name', 'email', 'tc', 'is_staff', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('UserCredentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'tc')}),
        ('Permissions', {'fields': ('is_admin',)})
    )

    # how text display at create object page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password', 'password2', 'tc')
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)


