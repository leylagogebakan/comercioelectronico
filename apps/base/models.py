from django.db import models

# Modelo base 
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True )
    state = models.BooleanField('Estado',default = True)
    create_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_data = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)
    
    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'

