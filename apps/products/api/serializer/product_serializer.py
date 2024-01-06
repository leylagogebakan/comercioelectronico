# Rest Frameworck
from rest_framework import serializers
# Modes 
from apps.products.models import Product
# Generic Serializer
from apps.products.api.serializer.general_serialzier import MeasureUnitSerializer, CategoryProductsSerializer

    
class ProductSerializer(serializers.ModelSerializer):
    """ Serialzier for Products"""


    class Meta:
        model = Product
        exclude = (
            'state',
            'create_date',
            'modified_date',
            'delete_data',
        )

    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'name' : instance.name,
            'description' : instance.description,
            'image' : instance.image if instance.image else '',
            'measure_unit' : instance.measure_unit.description,
            'category_product' : instance.category_product.description,
        }
