# Dejango
from django.contrib import admin
# Modes 
from .models import *

producto_modes = [
    Product,
    MeasureUnit,
    CategoryProducts,
    Idicator,
]

admin.site.register(producto_modes)
