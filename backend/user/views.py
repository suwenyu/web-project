from blog import serializers
# from blog.models import User
from django.contrib.auth.models import User
from django.db.models import query
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class UserView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """[User View]
    Desc:
        user view for list, get, update, delete
        checking authentication

    Returns:
        User Object
    """

    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user=User.objects.get(id=request.user.id)
        password = request.data.pop('password')
        if password:
            user.set_password(password)
        user_serializer=UserSerializer(user, data=request.data, partial=True)
        try:
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({'status':0,'message':'Error on user update'})


class CreateUserView(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """[create user view]
    Desc:
        user view for create user
        without checking authentication

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# TODO only the user itself can edit its info