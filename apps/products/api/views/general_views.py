#  Res Frameworck
from rest_framework import viewsets
# App : Products
from apps.products.models import MeasureUnit, CategoryProducts, Idicator
from apps.products.api.serializer.general_serialzier import  MeasureUnitSerializer, CategoryProductsSerializer, IdicatorSerializer


class MeasureUnitViewsets(viewsets.ModelViewSet):
    """ Class to list the units of measure """
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer

    
class IdicatorViewsets(viewsets.ModelViewSet):
    """ Class to list the units of Indicator """
    queryset =  Idicator.objects.all()
    serializer_class = IdicatorSerializer


class CategoryProductsViewsets(viewsets.ModelViewSet):
    """ Class to list the units of Category """
    queryset =  CategoryProducts.objects.all()
    serializer_class = CategoryProductsSerializer

    
