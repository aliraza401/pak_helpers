from django.contrib import admin
from .models import Helper, Rewiew, Category, Sub_Category
# Register your models here.

admin.site.register(Helper)
admin.site.register(Rewiew)
admin.site.register(Category)
admin.site.register((Sub_Category))