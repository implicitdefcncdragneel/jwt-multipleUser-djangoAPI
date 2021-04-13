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

    institute = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'institute')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('institute')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            institute_name=profile_data['institute_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender'],
            whats_app=profile_data['whats_app'],
            city=profile_data['city'],
            area=profile_data['area'],
            pincode=profile_data['pincode'],
            address=profile_data['address'],
            class_type=profile_data['class_type'],
            segment=profile_data['segment'],
            fees=profile_data['fees'],
            name=profile_data['name'],
            dob=profile_data['dob'],
            communication_address=profile_data['communication_address'],
            pincode1=profile_data['pincode1'],
            phone_number1=profile_data['phone_number1'],
            
            
            
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
