from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import login_view, register_view, logout_view


urlpatterns = [
    path('login', login_view),
    path('register', register_view),
    path('logout', logout_view),
]

