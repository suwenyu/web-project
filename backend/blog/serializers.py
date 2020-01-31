from rest_framework import serializers

from blog.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'phone_num', 'gender']

