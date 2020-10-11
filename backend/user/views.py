from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# from blog.models import User
from django.contrib.auth.models import User
from user.serializers import UserSerializer
# Create your views here.
from django.contrib.auth.decorators import login_required

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer