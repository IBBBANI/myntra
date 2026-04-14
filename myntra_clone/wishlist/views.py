from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from .models import Wishlist
from products.models import Product


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def add_to_wishlist(request, product_id):   
        product = Product.objects.get(id=product_id)

        Wishlist.objects.create(
            user=request.user,
            product=product
        )

        return redirect('/products/')
