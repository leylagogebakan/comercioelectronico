# Sjango 
from django.urls import path
# Views
from apps.products.api.views.product_views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
)
from apps.products.api.views.general_views import (
    MeasureUnitListAPIView, 
    IdicatorListAPIView, 
    CategoryProductsListAPIView
)

urlpatterns = [
    path(
        'measure/',
        MeasureUnitListAPIView.as_view(), 
        name='measure'
    ),
    path(
        'indicator/', 
        IdicatorListAPIView.as_view(), 
        name='indicator'
    ),
    path(
        'category/', 
        CategoryProductsListAPIView.as_view(), 
        name='category'
    ),
    path(
        'product/', 
        ProductListCreateAPIView.as_view(), 
        name='product-create'
    ),
    path(
        'product/<int:pk>', 
        ProductRetrieveUpdateDestroyAPIView.as_view(), 
        name='product-retrive-update-destroy'
    ),
]

