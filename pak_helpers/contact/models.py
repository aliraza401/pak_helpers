from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.message

class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    question = models.CharField(max_length=1500)
    answer = models.CharField(max_length=1500)
    is_frequent = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.question
