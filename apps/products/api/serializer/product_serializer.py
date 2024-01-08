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
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image and hasattr(instance.image, 'url') else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit and instance.measure_unit.description is not None else "",
            'category_product': instance.category_product.description if instance.category_product and instance.category_product.description is not None else "",
        }
