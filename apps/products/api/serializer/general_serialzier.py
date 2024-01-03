# Rest Frameworck
from rest_framework import serializers
# Modes 
from apps.products.models import MeasureUnit, CategoryProducts, Idicator



class  MeasureUnitSerializer(serializers.ModelSerializer):
    """ Serializer for Measure Unit """

    class Meta:
        model = MeasureUnit
        exclude = (
            'state',
            'create_date',
            'modified_date',
            'delete_data',
        )


class  CategoryProductsSerializer(serializers.ModelSerializer):
    """ Serializer for Category Products """

    class Meta:
        model = CategoryProducts
        exclude = (
            'state',
            'create_date',
            'modified_date',
            'delete_data',
        )



class  IdicatorSerializer(serializers.ModelSerializer):
    """ Serializer for Idicator """

    class Meta:
        model = Idicator
        exclude = (
            'state',
            'create_date',
            'modified_date',
            'delete_data',
        )

