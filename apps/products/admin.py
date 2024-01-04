# Dejango
from django.contrib import admin
# Modes 
from .models import *


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

producto_modes = [
    Product,
    Idicator,
]

admin.site.register(MeasureUnit,MeasureUnitAdmin)
admin.site.register(CategoryProducts, CategoryProductsAdmin)
admin.site.register(producto_modes)
