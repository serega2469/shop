from django.contrib import admin

from store.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    readonly_fields = ('created_at',)
    fields = ('name', 'slug', 'created_at')


# TODO: Написать настройки админ-панели для Product

admin.site.register(Category, CategoryAdmin)
