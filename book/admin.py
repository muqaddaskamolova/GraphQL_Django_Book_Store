from django.contrib import admin

from .models import *
from django.contrib import admin
from .forms import ProductAdminForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # sets values for how the admin site lists your products
    list_display = ('title', 'price_in_dollars')
    list_display_links = ('title',)
    list_per_page = 50
    ordering = ['category']

    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


# registers your product model with the admin site
admin.site.register(Books, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ('name', 'catalog')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', ]

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CatalogCategory, CategoryAdmin)
# Register your models here.
admin.site.register(Catalog)
admin.site.register(BookDetail)
admin.site.register(BookAttribute)
