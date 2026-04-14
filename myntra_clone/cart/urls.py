from rest_framework.routers import DefaultRouter
from .views import CartViewSet
from django.urls import path

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = router.urls