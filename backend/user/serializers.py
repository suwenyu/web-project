# from blog.models import User
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        validated_data['is_active'] = True
        user = User.objects.create(**validated_data)

        if password:
            user.set_password(password)
            user.save()

            return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only':True}}
        