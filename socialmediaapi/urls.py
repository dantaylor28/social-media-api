"""
URL configuration for socialmediaapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_route
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomJWTLoginView

# urlpatterns = [
#     path('', home_route),
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls')),
    
#     # Force JWT login view
#     path('dj-rest-auth/login/', CustomJWTLoginView.as_view(), name='jwt_login'),
#     path('dj-rest-auth/', include('dj_rest_auth.urls')),
#     path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

#     path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     path('', include('posts.urls')),
#     path('', include('profiles.urls')),
#     path('', include('pins.urls')),
#     path('', include('comments.urls')),
#     path('', include('followers.urls')),
#     path('', include('comment_likes.urls')),
#     path('', include('categories.urls')),
# ]


from django.contrib import admin
from django.urls import path, include
from .views import home_route, CustomJWTLoginView
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import JsonResponse
from django.conf import settings

def debug_login(request):
    """Temporary endpoint to inspect live environment settings. Delete later"""
    return JsonResponse({
        "REST_USE_JWT": getattr(settings, "REST_USE_JWT", None),
        "SITE_ID": getattr(settings, "SITE_ID", None),
        "AUTH_USER_MODEL": getattr(settings, "AUTH_USER_MODEL", None),
        "DATABASES": list(settings.DATABASES.keys()),
    })


urlpatterns = [
    # Home route
    path('', home_route),

    # Admin
    path('admin/', admin.site.urls),

    # Browsable API login
    path('api-auth/', include('rest_framework.urls')),

    # ✅ Force JWT login view override (must come BEFORE the general dj-rest-auth include)
    path('dj-rest-auth/login/', CustomJWTLoginView.as_view(), name='custom_login'),

    # ✅ Include all default dj-rest-auth endpoints (logout, password reset, etc.)
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    # ✅ Registration endpoints
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # ✅ JWT refresh endpoint (for refreshing access tokens)
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Temporary debug route! delete this when login works 
    path("debug-login/", debug_login),

    # ✅ Your app URLs
    path('', include('posts.urls')),
    path('', include('profiles.urls')),
    path('', include('pins.urls')),
    path('', include('comments.urls')),
    path('', include('followers.urls')),
    path('', include('comment_likes.urls')),
    path('', include('categories.urls')),
]

