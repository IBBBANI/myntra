from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user,"-----------------------")
        serializer.save(user=self.request.user)