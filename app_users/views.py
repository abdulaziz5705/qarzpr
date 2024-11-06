from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework.views import APIView

from app_users.models import UserModel
from app_users.serializer import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            response = {
                "token": token.key,
                "username": user.username,
                "phone_number": user.phone_number
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Invalid Credentials"
        }, status=status.HTTP_400_BAD_REQUEST)


