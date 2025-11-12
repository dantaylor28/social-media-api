from django.shortcuts import render
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from socialmediaapi.permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import traceback

# Delete thius view later
@csrf_exempt
def debug_login(request):
    import json
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"error": "Authentication failed"}, status=400)

        return JsonResponse({
            "message": "User authenticated successfully",
            "user": user.username,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
        })
    except Exception as e:
        print("🔥 DEBUG LOGIN ERROR:", str(e))
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)

class ProfileListView(generics.ListAPIView):
    """
    Lists out all users and their profile information.
    Profiles can be filtered, searched and ordered from
    a number of options.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        num_of_posts=Count('owner__post', distinct=True),
        num_of_followers=Count('owner__followed', distinct=True),
        num_of_following=Count('owner__following', distinct=True),
        num_of_pinned_posts=Count('owner__pin', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]

    search_fields = [
        'owner__username',
        'owner__profile__name',
        'owner__profile__location'
    ]

    ordering_fields = [
        'num_of_followers',
        'num_of_following',
        'num_of_posts'
    ]

    filterset_fields = [
        # shows profiles that are following the selected user
        'owner__following__followed__profile',
        # shows profiles that are followed by the selected user
        'owner__followed__owner__profile'
    ]

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Lists all information for a selected user and the ability to update
    & delete the profile if you are the owner
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        num_of_posts=Count('owner__post', distinct=True),
        num_of_followers=Count('owner__followed', distinct=True),
        num_of_following=Count('owner__following', distinct=True),
        num_of_pinned_posts=Count('owner__pin', distinct=True)
    ).order_by('-created_at')
