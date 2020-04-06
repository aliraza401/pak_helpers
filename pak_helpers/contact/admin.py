from django.contrib import admin
from .models import Contact, Question
# Register your models here.

admin.site.register(Question)
admin.site.register(Contact)