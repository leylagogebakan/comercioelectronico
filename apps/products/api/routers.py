# Res Frameworck
from rest_framework.routers import DefaultRouter
# App : Product
from apps.products.api.views.product_viewset import ProductViewSet
from apps.products.api.views.general_views import (
    MeasureUnitViewsets,
    IdicatorViewsets,
    CategoryProductsViewsets,
)

router = DefaultRouter()

router.register(r"product", ProductViewSet, basename= 'product')
router.register (r"measureunit", MeasureUnitViewsets, basename= 'measureunit')
router.register(r"idicator", IdicatorViewsets, basename= 'idicator')
router.register(r"category", CategoryProductsViewsets, basename= 'category')

urlpatterns = router.urls