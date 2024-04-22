from django.contrib import admin

from library import models
from user.admin import UserAdmin, LibraryUserAdmin


@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'authors']
    list_per_page = 10
    list_filter = ['isbn']
    search_fields = ['title']
    ordering = ['title']


class LibraryUser(LibraryUserAdmin):
    p = " « » »"
    pass


# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Genre)
