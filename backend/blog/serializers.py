from rest_framework import serializers

# from blog.models import User
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        validated_data['is_active'] = True
        user = User.objects.create(**validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

        