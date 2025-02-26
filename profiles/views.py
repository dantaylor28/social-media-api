from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.db.models import Count

class ProfileListView(generics.ListAPIView):
    """
    Lists out all users and their profile information
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        num_of_posts=Count('owner__post', distinct=True),
        num_of_followers=Count('owner__followed', distinct=True),
        num_of_following=Count('owner__following', distinct=True),
        num_of_pinned_posts=Count('owner__pin', distinct=True)
    ).order_by('-created_at')

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Lists all information for a selected user and the ability to update
    & delete the profile if you are the owner
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
