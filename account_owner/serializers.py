from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


user = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class UserSerializer(serializers.ModelSerializer):
    
    groups = GroupSerializer()
    
    class Meta:
        model = user
        fields = ["id","email", "groups", "first_name", "last_name"]
