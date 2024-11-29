from django.urls import path
from .views import RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="get_token"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="get_token")
]
