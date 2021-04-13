import uuid
from django.db import models
from ..user.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='institute')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institute_name = models.CharField(max_length=50, blank=True,null=True)
    phone_number = models.CharField(max_length=10, unique=True, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    whats_app= models.CharField(max_length=10, blank=False,default=False)
    city= models.CharField(max_length=50, unique=False,default=False)
    area=models.CharField(max_length=50, unique=False,default=False)
    pincode=models.PositiveIntegerField( blank=False,default=False)
    address=models.CharField(max_length=50, unique=False,default=False)
    class_type=models.CharField(max_length=50, unique=False,default=False)
    segment=models.CharField(max_length=50, unique=False,default=False)
    fees=models.CharField(max_length=50, unique=False,default=False)
    name=models.CharField(max_length=50, unique=False,default=False)
    dob=models.CharField(max_length=50, unique=False,default=False)
    communication_address =models.CharField(max_length=250, unique=False,default=False)
    pincode1=models.PositiveIntegerField( blank=False,default=False)
    phone_number1 = models.CharField(max_length=10, unique=True, blank=False)
    
    def __str__(self):
        return self.institute_name

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile_institute"















