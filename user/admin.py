from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class LibraryUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name" ""),
            },
        ),
    )
    pass
