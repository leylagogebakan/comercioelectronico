# Res Frameworck
from rest_framework.routers import DefaultRouter
# App : Product
from apps.products.api.views.product_viewset import ProductViewSet

router = DefaultRouter()

router.register(r"product", ProductViewSet, basename= 'product')

urlpatterns = router.urls