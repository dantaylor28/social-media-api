from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def home_route(request):
    return Response({
        'message': 'Welcome to my social media API!'
    })

# socialmediaapi/views.py

from dj_rest_auth.views import LoginView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

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
