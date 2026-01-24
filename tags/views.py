from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Tag
from .serializers import TagSerializer

class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
