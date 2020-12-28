from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


user = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = user.objects.create_user(**validated_data)
        return user

    class Meta:
        model = user
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class UserSerializer(serializers.ModelSerializer):
    
    groups = GroupSerializer()
    
    class Meta:
        model = user
        fields = ["id","email", "groups", "first_name", "last_name"]
