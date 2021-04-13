import uuid
from django.db import models
from ..user.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='students')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    select_subject= models.CharField(max_length=50, unique=False,default=False)
    select_city= models.CharField(max_length=50, unique=False,default=False)
    enter_area =models.CharField(max_length=50, unique=False,default=False)
    preference=models.CharField(max_length=50, unique=False,default=False)
    requirement=models.CharField(max_length=250, unique=False,default=False)
    name=models.CharField(max_length=50, unique=False,default=False)
    dob=models.CharField(max_length=50, unique=False,default=False)
    communication_address =models.CharField(max_length=250, unique=False,default=False)
    pincode=models.PositiveIntegerField( blank=False,default=False)
    phone_number = models.CharField(max_length=10, unique=True, blank=False)
    

    def __str__(self):
        return self.name

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile_student"















