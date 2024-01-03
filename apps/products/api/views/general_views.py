# Res Frameworck
from rest_framework import generics
# Models
from apps.products.models import MeasureUnit, Idicator, CategoryProducts
# Serializer
from apps.products.api.serializer.general_serialzier import  MeasureUnitSerializer, CategoryProductsSerializer, IdicatorSerializer


class MeasureUnitListAPIView(generics.ListAPIView):
    """ Class to list the units of measure """
    
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)


class IdicatorListAPIView(generics.ListAPIView):
    """ Class to list the units of Indicator """
    
    serializer_class = IdicatorSerializer

    def get_queryset(self):
        return Idicator.objects.filter(state = True)


class CategoryProductsListAPIView(generics.ListAPIView):
    """ Class to list the units of Category """
    
    serializer_class = CategoryProductsSerializer

    def get_queryset(self):
        return CategoryProducts.objects.filter(state = True)
