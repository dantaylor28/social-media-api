from django.shortcuts import render
from .models import Pin
from .serializers import PinSerializer
from rest_framework import generics

class PinListView(generics.ListCreateAPIView):
    """
    Lists out the information of all pinned posts, also
    specific posts can be pinned here if you are authenticated.
    """
    serializer_class = PinSerializer
    queryset = Pin.objects.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PinDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrives the details of a specific pin. This can be
    deleted if you are the owner of it.
    """
    serializer_class = PinSerializer
    queryset = Pin.objects.all()