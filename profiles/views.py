from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics

class ProfileListView(generics.ListAPIView):
    """
    Lists out all users and their profile information
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('-created_at')

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Lists all information for a selected user and the ability to update
    & delete the profile if you are the owner
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
