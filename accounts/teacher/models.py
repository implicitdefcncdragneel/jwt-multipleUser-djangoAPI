import uuid
from django.db import models
from ..user.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, unique=False,null=True)
    phone_number = models.CharField(max_length=10, unique=True, blank=False)
    age = models.PositiveIntegerField(null=True, blank=False)
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    user_type = models.CharField(max_length=50, unique=False,default="Teacher")
    whats_app= models.CharField(max_length=10, blank=False,default=False)
    city= models.CharField(max_length=50, unique=False,default=False)
    area=models.CharField(max_length=50, unique=False,default=False)
    pincode=models.PositiveIntegerField( blank=False,default=False)
    address=models.CharField(max_length=50, unique=False,default=False)
    class_type=models.CharField(max_length=50, unique=False,default=False)
    segment=models.CharField(max_length=50, unique=False,default=False)
    fees=models.CharField(max_length=50, unique=False,default=False)
    institutename=models.CharField(max_length=50, unique=False,default=False)
    experience=models.CharField(max_length=50, unique=False,default=False)
    expdetail=models.CharField(max_length=50, unique=False,default=False)
    tutor_detail=models.CharField(max_length=50, unique=False,default=False)
    # is_usertype=models.CharField(max_length=50, unique=False,default=False)


    # def validate_not_empty(value):
    #     if value == '':
    #         raise ValidationError('%(value)s is empty!'),params={'value':value}

    def __str__(self):
        return self.first_name

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile_teacher"















