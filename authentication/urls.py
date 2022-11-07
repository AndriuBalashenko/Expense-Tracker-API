from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    LoginAPIView,
    LogOutAPIView,
    PasswordTokenCheckAPI,
    RegisterView,
    RequestPasswordResetEmail,
    SetNewPasswordAPIView,
    VerifyEmail,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("verify-email/", VerifyEmail.as_view(), name="email-verification"),
    path("token/refresh/", TokenRefreshView.as_view(), name="tokenrefresh"),
    path(
        "request-reset-email/",
        RequestPasswordResetEmail.as_view(),
        name="request-reset-email",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    path("logout/", LogOutAPIView.as_view(), name="logout"),
]
