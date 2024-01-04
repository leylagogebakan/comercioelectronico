# Rest Frameworck
from rest_framework import generics
# Apps : Base
from apps.products.api.serializer.product_serializer import ProductSerializer
from apps.base.api import GenericListAPIView


class ProdutListAPIView(GenericListAPIView):
    """ List Api View for Product. Method GET. """
    serializer_class = ProductSerializer



class ProductCreateAPIView(generics.CreateAPIView):
    """Create Apu Vire for Product. Method POST. """
    serializer_class =  ProductSerializer
