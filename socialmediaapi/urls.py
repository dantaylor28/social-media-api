from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import home_route, CustomJWTLoginView

urlpatterns = [
    path('', home_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    # Force JWT login view
    path('dj-rest-auth/login/', CustomJWTLoginView.as_view(), name='custom_login'),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), # Include all default dj-rest-auth endpoints (logout, password reset, etc.)
    path('dj-rest-auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include('posts.urls')),
    path('', include('profiles.urls')),
    path('', include('pins.urls')),
    path('', include('comments.urls')),
    path('', include('followers.urls')),
    path('', include('comment_likes.urls')),
    path('', include('categories.urls')),
]