from django.urls import path
from .views import PlaceOrderView,OrderHistoryView

urlpatterns = [
    path('place-order/', PlaceOrderView.as_view()),
    path('history/', OrderHistoryView.as_view()),
]