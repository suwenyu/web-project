from django.shortcuts import render
from rest_framework import viewsets

# from blog.models import User
from django.contrib.auth.models import User
from blog.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    