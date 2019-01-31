from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ['__str__', 'description', 'price']
    list_display = ['__str__', 'description', 'price', 'created', 'updated']
    list_editable = ['price']
    readonly_fields = ['created', 'updated']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
