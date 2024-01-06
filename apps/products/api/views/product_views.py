# Rest Frameworck
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Apps : Base
from apps.products.api.serializer.product_serializer import ProductSerializer
from apps.base.api import GenericListAPIView
 

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """List and Create Api View for Product. Method POST - GET. """
    serializer_class =  ProductSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def post(self, request):
        serializer = self.serializer_class(data =  request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'menssage':'Producto creado correctamente! '
                },
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


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



class PrtoductUpdateAPIView(generics.UpdateAPIView):
    """ Update Api vire for Produc """
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk):     
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()    

    # Obtener la instacia 
    def patch(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status= status.HTTP_200_OK)
        return Response (
            {
                'error':'No existe un Prudcuto con estos datos!'
            },
            status= status.HTTP_400_BAD_REQUEST 
        )

    # Actualizamos la intancia
    def put(self, request, pk = None):
        
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response(product_serializer.errors, status= status.HTTP_400_BAD_REQUEST)