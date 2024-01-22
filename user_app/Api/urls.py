from django.urls import path, include

from user_app.Api.views import RegisterUser, VerifyOTP

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register-user"),
    path("verify/", VerifyOTP.as_view(), name="verify-user"),
]
