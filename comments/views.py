from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters

class CommentListView(generics.ListCreateAPIView):
    """
    List of all comments, with the relevant fields included.
    Authenticated users are able to write a comment here.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter
    ]

    filterset_fields = ['post', 'owner']

    ordering_fields = ['timestamp']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves the information of a specified comment, which can be
    edited or deleted if you are the owner of it.
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()