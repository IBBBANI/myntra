from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import path

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = router.urls