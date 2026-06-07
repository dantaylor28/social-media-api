from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import Like
from .serializers import LikeSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics

class LikeListView(generics.ListCreateAPIView):
    """
    Lists out the information of all liked posts, also
    specific posts can be liked here if you are authenticated.
    Likes can be filtered by post or a specific profile.
    """
    serializer_class = LikeSerializer
    queryset = Like.objects.all().order_by('-timestamp')

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        'post',
        'owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrives the details of a specific like. This can be
    deleted if you are the owner of it.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()