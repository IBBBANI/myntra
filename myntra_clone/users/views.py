from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login, logout
from .models import User


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/products/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

#register view

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username, password=password)

        return redirect('/login/')

    return render(request, 'register.html')



#logout view

def logout_view(request):
    logout(request)
    return redirect('/login/')
