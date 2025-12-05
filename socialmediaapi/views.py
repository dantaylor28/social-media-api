from rest_framework.decorators import api_view
from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status

@api_view()
def home_route(request):
    return Response({
        'message': 'Welcome to my social media API!'
    })

class CustomJWTLoginView(LoginView):
    """
    Custom login view that returns JWT access & refresh tokens
    along with basic user info.
    """

    def get_response(self):
        # self.user is set by the parent LoginView after successful login
        refresh = RefreshToken.for_user(self.user)
        access = refresh.access_token

        data = {
            "access": str(access),
            "refresh": str(refresh),
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
            }
        }
        return Response(data)
    

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        # Use default behavior to create the user
        response = super().create(request, *args, **kwargs)
        user = self.user  # RegisterView sets self.user

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "username": user.username
        }, status=status.HTTP_201_CREATED)

