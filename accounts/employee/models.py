import uuid
from django.db import models
from ..user.models import User
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    skills_info = models.CharField(max_length=50, unique=False,default=False)
    education = models.CharField(max_length=50, unique=False,default=False)
    select_experience  =models.CharField(max_length=50, unique=False,default=False)
    select_emp_type =models.CharField(max_length=50, unique=False,default=False)
    membership =models.CharField(max_length=250, unique=False,default=False)
    name=models.CharField(max_length=50, unique=False,default=False)
    dob=models.CharField(max_length=50, unique=False,default=False)
    communication_address =models.CharField(max_length=250, unique=False,default=False)
    pincode=models.PositiveIntegerField( blank=False,default=False)
    phone_number1 = models.CharField(max_length=10, unique=True, blank=False)
    

    def __str__(self):
        return self.name

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile_employee"















