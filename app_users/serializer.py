from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app_users.models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=13, validators=[UniqueValidator(queryset=UserModel.objects.all())])
    password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']



    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Password do not match')
        return attrs

    def validate_phone_number(self, phone_number: str):
        phone_number = phone_number.strip()
        if not phone_number.startswith('+998'):
            raise serializers.ValidationError('Invalid phone number start with +998')
        if not phone_number[4:].isdigit():
            raise serializers.ValidationError('Invalid phone number')
        return phone_number



    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number']
