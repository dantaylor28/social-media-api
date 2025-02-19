from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics

class CommentListView(generics.ListCreateAPIView):
    """
    List of all comments, with the relevant fields included.
    Authenticated users are able to write a comment here.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves the information of a specified comment, which can be
    edited or deleted if you are the owner of it.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()