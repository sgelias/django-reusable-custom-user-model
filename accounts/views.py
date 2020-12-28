import requests
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


user = get_user_model()


class UserDetails(viewsets.ReadOnlyModelViewSet):

    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    
    @action(detail=True, methods=['get'])
    def get_single(self, request):
        """
        Return a single record given id.
        """
        
        item = get_object_or_404(user, pk=request.user.id)
        serializer = UserSerializer(item)
        return Response(serializer.data, status=200)
