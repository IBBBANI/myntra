from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView   # ✅ ADD THIS
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer          # ✅ ADD THIS

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            return Response({"error": "Cart is empty"})

        total_price = 0
        order = Order.objects.create(user=user, total_price=0)

        for item in cart_items:
            total_price += item.product.price * item.quantity

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        order.total_price = total_price
        order.save()

        cart_items.delete()  # Clear cart

        return Response({"message": "Order placed successfully"})
    
class OrderHistoryView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
