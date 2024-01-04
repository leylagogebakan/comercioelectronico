# Sjango 
from django.urls import path
# Views
from apps.products.api.views.product_views import (
    ProdutListAPIView,
    ProductCreateAPIView
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
    path('product/list/', ProdutListAPIView.as_view(), name='product-list'),
    path('product/create', ProductCreateAPIView.as_view(), name='product-create'),
]

