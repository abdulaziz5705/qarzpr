from re import search

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from rest_framework.views import APIView

from app_users.models import UserModel
from app_users.serializer import RegisterSerializer, LoginSerializer, UserSerializer, UserSearchSerializer


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

class UserListView(APIView):
    def get(self, request, *args, **kwargs):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetailView(APIView):

        def get(self, request, *args, **kwargs):
            try:
                user = UserModel.objects.get(pk=self.kwargs['pk'])
            except UserModel.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = UserSerializer(user)
            return Response(serializer.data)

class UserSearchView(APIView):
    def get(self, request):
        users = UserModel.objects.all()

        search = request.query_params.get('search')
        page = int(request.query_params.get('page'))
        page_size = int(request.query_params.get('page_size', 2))
        if search is not None:
            users = users.filter(username__icontains=search)
        if page :
            page -=1
            users = users[page * page_size: page* page_size+ page_size]
        serializer = UserSearchSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthenticateUserView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        return Response({"message": "You are authenticated"}, status=status.HTTP_200_OK)

class AuthenticatedSuperUserView(APIView):
    @permission_classes([IsAdminUser])
    def get(self, request):
        return Response({"message": "Authenticate super user view"}, status=status.HTTP_200_OK)

class UnauthenticatedUserView(APIView):

    def get(self, request):
        return Response({"message": "Unauthonticate view"})


