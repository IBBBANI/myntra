from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from .models import Cart
from products.models import Product
from django.shortcuts import render


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print(self.request.user,"-----------------------")
        serializer.save(user=self.request.user)


    def add_to_cart(request, product_id):
        product = Product.objects.get(id=product_id)

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

        return redirect('/products/')    


    def view_cart(request):
        items = Cart.objects.filter(user=request.user)
        return render(request, 'cart.html', {'items': items})

