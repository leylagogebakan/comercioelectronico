# Rest Frameworck
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Apps : Base
from apps.products.api.serializer.product_serializer import ProductSerializer
from apps.base.api import GenericListAPIView


class ProdutListAPIView(GenericListAPIView):
    """ List Api View for Product. Method GET. """
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """Create Api View for Product. Method POST. """
    serializer_class =  ProductSerializer


class ProductRetriveAPIView(generics.RetrieveAPIView):
    """ Retive Api View for Product"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Destroy Api View for Product"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response (
                {
                    'mesage': 'Producto eliminado correctamente'
                },
                status= status.HTTP_200_OK
            )
        return Response (
            {
                'error':'No existe un Prudcuto con estos datos!'
            },
            status= status.HTTP_400_BAD_REQUEST
        )

        