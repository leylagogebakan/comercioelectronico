"""
# Res Frameworck
from rest_framework import generics
# Models
from apps.products.models import MeasureUnit, Idicator, CategoryProducts
"""
# Apss : Base
from apps.base.api import GenericListAPIView
# Serializer
from apps.products.api.serializer.general_serialzier import  MeasureUnitSerializer, CategoryProductsSerializer, IdicatorSerializer


class MeasureUnitListAPIView(GenericListAPIView):
    """ Class to list the units of measure """
    
    serializer_class = MeasureUnitSerializer

    
class IdicatorListAPIView(GenericListAPIView):
    """ Class to list the units of Indicator """
    
    serializer_class = IdicatorSerializer


class CategoryProductsListAPIView(GenericListAPIView):
    """ Class to list the units of Category """
    
    serializer_class = CategoryProductsSerializer

    
