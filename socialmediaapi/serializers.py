from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CurrentUserSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_id', 'profile_image')

    def get_profile_image(self, obj):
        if obj.profile.profile_image:
            return obj.profile.profile_image.url
        return None