# Rest Frameworck
from rest_framework import serializers
# Modes 
from apps.products.models import MeasureUnit, CategoryProducts, Idicator



class  MeasureUnitSerializer(serializers.ModelSerialzier):
    """ Serializer for Measure Unit """

    class Meta:
        model = MeasureUnit
        exclude = ('state',)


class  CategoryProductsSerializer(serializers.ModelSerialzier):
    """ Serializer for Category Products """

    class Meta:
        model = CategoryProducts
        exclude = ('state',)


class  IdicatorSerializer(serializers.ModelSerialzier):
    """ Serializer for Idicator """

    class Meta:
        model = Idicator
        exclude = ('state',)
