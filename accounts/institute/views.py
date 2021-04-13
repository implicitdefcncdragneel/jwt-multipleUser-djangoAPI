from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserRegistrationSerializer
from .models import UserProfile


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'institute_name': user_profile.institute_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                    'whats_app':user_profile.whats_app,
                    'city': user_profile.city,
                    'area': user_profile.area,
                    'pincode':user_profile.pincode,
                    'address':user_profile.address,
                    'class_type':user_profile.class_type,
                    'segment':user_profile.segment,
                    'fees':user_profile.fees,
                    'name':user_profile.name,
                    'dob': user_profile.dob,
                    'communication_address': user_profile.communication_address,
                    'pincode1':user_profile.pincode1,
                    'phone_number1':user_profile.phone_number1,

                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)
