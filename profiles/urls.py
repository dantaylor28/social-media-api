from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view()),
    path('profiles/<str:username>/', views.ProfileDetailView.as_view())
]