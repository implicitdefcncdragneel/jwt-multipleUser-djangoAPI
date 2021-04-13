from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import UserProfile
from ..user.models import User


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('__all__')
        read_only_fields = ('user',)
        

class UserRegistrationSerializer(serializers.ModelSerializer):

    students = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'students')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('students')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            select_subject=profile_data['select_subject'],
            select_city=profile_data['select_city'],
            enter_area=profile_data['enter_area'],
            preference=profile_data['preference'],
            requirement=profile_data['requirement'],
            name=profile_data['name'],
            dob=profile_data['dob'],
            communication_address=profile_data['communication_address'],
            pincode=profile_data['pincode'],
            phone_number=profile_data['phone_number'],
            
        )
        return user

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
