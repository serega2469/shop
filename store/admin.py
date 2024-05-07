from django.contrib import admin

from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('created_at',)
    fields = ('name', 'slug', 'created_at')


# TODO: Написать настройки админ-панели для Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'is_available')
    # readonly_fields = ('created_at',)
    fields = ('name', 'quantity', 'category', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

