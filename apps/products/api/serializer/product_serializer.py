# Rest Frameworck
from rest_framework import serializers
# Modes 
from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """ Serialzier for Products"""

    class Meta:
        model = Product
        exclude = ('state',)
