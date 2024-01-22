from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_app.Api.serializer import UserSerializer
from user_app.Api.emails import send_otp_via_email
from user_app.Api.serializer import VerifyUserSerializer
from user_app.models import User


class RegisterUser(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data["email"])
                return Response(
                    {
                        "status": 200,
                        "message": "Registration successful, please check your email to confirm",
                        "data": serializer.data,
                    }
                )

            return Response(
                {
                    "status": 400,
                    "message": "Invalid credentials",
                    "data": serializer.errors,
                }
            )

        except Exception as e:
            return HttpResponse("Invalid Token")


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyUserSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data["email"]
                otp = serializer.data["otp"]

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "message": "Invalid credentials",
                            "error": "Invalid Email",
                        }
                    )

                if not user[0].otp == otp:
                    return Response(
                        {
                            "status": 400,
                            "message": "Invalid credentials",
                            "error": "wrong otp",
                        }
                    )

                user = user.first()
                user.is_verified = True
                user.save()

                return Response(
                    {
                        "status": 200,
                        "message": "account verified",
                        "data": {},
                    }
                )

            else:
                return Response(
                    {
                        "status": 400,
                        "message": "Invalid credentials",
                        "data": serializer.errors,
                    }
                )

        except Exception as e:
            return HttpResponse("Invalid Token")
