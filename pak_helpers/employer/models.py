from django.db import models
from django.contrib.auth.models import User

# Create your models here.

   
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    profile_picture = models.ImageField(
        upload_to='employer_img', null=True, blank=True)
    province = models.CharField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    area = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.user.username
