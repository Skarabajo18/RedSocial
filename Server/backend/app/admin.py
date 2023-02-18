
from .models import (
    User,
    UserProfile,
    UserRelationship
)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'type',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',)
        }),
        ('Additional info', {
            'fields': ('type',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',)
        }),
        ('Additional info', {
            'fields': ('type', )
        })
    )

###################################################################
#   Agregar el modelo instanciado para que en el panel            #
#   de administracion se vean reflejadas las clases de modelos    #
###################################################################


admin.site.register(User, UserAdmin)

admin.site.register(UserProfile)
admin.site.register(UserRelationship)
