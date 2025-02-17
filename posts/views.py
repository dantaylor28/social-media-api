from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

class PostListView(generics.ListCreateAPIView):
    """
    Lists out all posts and the ability to create your own
    if you are signed in and authenticated
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-uploaded_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Lists a selected post with the ability to edit or delete it
    if you are the post owner
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
