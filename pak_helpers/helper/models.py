from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import template
from django.contrib.auth.models import Group


class Helper(models.Model):
    option = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(
        upload_to='helper_img', null=True, blank=True, default='helper_img/def_img.png')
    contact_number = models.CharField(max_length=13)
    cnic = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=option, default='Male')
    description = models.TextField(max_length=5000)
    daily_work_rate = models.IntegerField()
    profile_visible = models.BooleanField(null=True)
    age = models.SmallIntegerField(null=True)
    category = models.ManyToManyField('Category',null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        output_size = (500, 500)
        img.thumbnail(output_size)
        img.save(self.profile_picture.path)


class Rewiew(models.Model):
    user = models.ForeignKey(Helper, on_delete=models.SET_NULL, null=True)
    star = models.IntegerField()
    comment = models.TextField(max_length=1500, default='.')

    def __str__(self):
        return self.user.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
