import django_filters
from django_filters import DateFilter
from helper.models import Helper


class HelperFilter(django_filters.FilterSet):

    class Meta:
        model = Helper
        fields = '__all__'
        exclude = ['profile_picture', 'daily_work_rate' ,'user','contact_number','cnic','gender','description','profile_visible','age']
