""" Rest Frameworck """
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Apps : Base
from apps.products.api.serializer.product_serializer import ProductSerializer

class ProductViewSet (viewsets.ModelViewSet):
    """ View Set for Product. Method GET- POST - PUT - PATH - DELETE  """
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk =None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True ).first()

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(product_serializer.data, status = status.HTTP_200_OK)

    # Crea la instania
    def create(self, request):
        serializer = self.serializer_class(data =  request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'menssage':'Producto creado correctamente! '
                },
                status = status.HTTP_200_OK
            )
        return Response(
            serializer.errors, 
            status= status.HTTP_400_BAD_REQUEST
        )

    # Eliminamos la instania
    def destroy(self, request, pk=None):
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
    
    # Actualizamos la Instacia
    def update(self, request,pk = None):
            
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,  status = status.HTTP_200_OK)
        return Response(
            product_serializer.errors, 
            status= status.HTTP_400_BAD_REQUEST
        )
 