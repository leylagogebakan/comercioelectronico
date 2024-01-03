# Django
from django.db import models
# apps : base
from apps.base.models import BaseModel


class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""

    # TODO: Define fields here
    description = models.CharField(
        'Descripcionm', 
        max_length=50,
        blank = False,
        null = False,
        unique = True
    )
    
    class Meta:
        """Meta definition for MeasureUnit."""

        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'

    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description
    

class CategoryProducts(BaseModel):
    """Model definition for CategoryProducts."""

    # TODO: Define fields here
    description = models.CharField(
        'Descripcion', 
        max_length=50,
        blank = False,
        null = False,
        unique = True
    )

    class Meta:
        """Meta definition for CategoryProducts."""

        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        """Unicode representation of CategoryProducts."""
        return self.description


class Idicator(BaseModel):
    """Model definition for Idicator."""

    # TODO: Define fields here
    descount_value = models.PositiveSmallIntegerField()
    category_product = models.ForeignKey(
        CategoryProducts, 
        on_delete=models.CASCADE,
        verbose_name = ' Indicador de Oferta'
    )

    class Meta:
        """Meta definition for Idicator."""

        verbose_name = 'Indicador de ofertas1'
        verbose_name_plural = 'Indicadorres de ofertass'

    def __str__(self):
        """Unicode representation of Idicator."""
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'
 

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(
        'Nombre del Producto', 
        max_length=150,
        blank = False,
        null = False,
        unique = True
    )
    description = models.TextField(
        'Descripcion del Producto',
        blank = False,
        null = False,
    )
    image = models.ImageField(
        'Imagen del Producto', 
        upload_to='products/',
        blank = True,
        null = True,
    )
    measure_unit = models.ForeignKey(
        MeasureUnit, 
        on_delete=models.CASCADE,
        verbose_name = 'Unidad de Medida',
        null = True    
    )
    category_product = models.ForeignKey(
        CategoryProducts, 
        on_delete=models.CASCADE,
        verbose_name = 'Categoria de producto',
        null = True
    )

    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
