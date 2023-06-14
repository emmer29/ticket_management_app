from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# managing users from admin is difficult, so its better to create a custom admin user

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_customer',
                    'is_engineer'
                )
            }
        )
    )
admin.site.register(User, CustomUserAdmin)