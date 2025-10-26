# from dj_rest_auth.serializers import UserDetailsSerializer
# from rest_framework import serializers


# class CurrentUserSerializer(UserDetailsSerializer):
#     profile_id = serializers.ReadOnlyField(source='profile.id')
#     profile_image = serializers.ReadOnlyField(source='profile.image.url')

#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + (
#             'profile_id', 'profile_image'
#         )


from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CurrentUserSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_id', 'profile_image')
