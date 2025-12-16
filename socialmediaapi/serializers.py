from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CurrentUserSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ImageField(
        source='profile.profile_image',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_id', 'profile_image')