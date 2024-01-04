# Sjango 
from django.urls import path
# Views
from apps.products.api.views.product_views import ProdutListAPIView
from apps.products.api.views.general_views import (
    MeasureUnitListAPIView, 
    IdicatorListAPIView, 
    CategoryProductsListAPIView
)

urlpatterns = [
    path('measure/', MeasureUnitListAPIView.as_view(), name='measure'),
    path('indicator/', IdicatorListAPIView.as_view(), name='indicator'),
    path('category/', CategoryProductsListAPIView.as_view(), name='category'),
    path('product/', ProdutListAPIView.as_view(), name='product'),
]

