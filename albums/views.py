from rest_framework.views import APIView, status, Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Album
from .serializers import AlbumSerializer
import ipdb


class AlbumView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.all()

    def perform_create(self, serializer):
        # ipdb.set_trace()
        return serializer.save(user_id=self.request.user.id)

    # def get(self, request):
    #     """
    #     Obtençao de albums
    #     """
    #     albums = Album.objects.all()

    #     result_page = self.paginate_queryset(albums, request)
    #     serializer = AlbumSerializer(result_page, many=True)

    #     return self.get_paginated_response(serializer.data)

    # def post(self, request):
    #     """
    #     Criaçao de album
    #     """
    #     serializer = AlbumSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user=request.user)

    #     return Response(serializer.data, status.HTTP_201_CREATED)
