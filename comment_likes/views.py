from django.shortcuts import render
from .models import CommentLike
from .serializers import CommentLikeSerializer
from rest_framework import generics
from socialmediaapi.permissions import IsOwnerOrReadOnly

class CommentLikeListView(generics.ListCreateAPIView):
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentLikeDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CommentLike.objects.all()
