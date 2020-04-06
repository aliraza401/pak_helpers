from django.urls import path, include

from . import views

app_name = 'employer'

urlpatterns = [
    path('create/', views.employerCreateView, name='create_employer'),
    path('update/', views.employerUpdateView, name='update_employer'),
    path('employer_dashboard/',
         views.employerDashboardView, name='dashboard_employer'),
    path('deactive/', views.employerDeactivateView, name='deactive'),


    # # ajaz requests urls
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    # path('ajax/load-areas/', views.load_area, name='ajax_load_areas'),

]
 