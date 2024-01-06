# Sjango 
from django.urls import path
# Views
from apps.products.api.views.product_views import (
    ProductListCreateAPIView,
    ProductRetriveAPIView,
    ProductDestroyAPIView,
    PrtoductUpdateAPIView
)
from apps.products.api.views.general_views import (
    MeasureUnitListAPIView, 
    IdicatorListAPIView, 
    CategoryProductsListAPIView
)

urlpatterns = [
    path('measure/', MeasureUnitListAPIView.as_view(), name='measure'),
    path('indicator/', IdicatorListAPIView.as_view(), name='indicator'),
    path('category/', CategoryProductsListAPIView.as_view(), name='category'),
    path('product/', ProductListCreateAPIView.as_view(), name='product-create'),
    path('product/retrive/<int:pk>', ProductRetriveAPIView.as_view(), name='product-retrive'),
    path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name='product-destroy'),
    path('product/update/<int:pk>', PrtoductUpdateAPIView.as_view(), name='product-update'),
]

