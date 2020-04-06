from django.urls import path
from . import views

app_name = 'helper'

urlpatterns = [
    path('create/', views.createHelplerView, name='create_helper'),
    path('update/', views.UpdateHelplerView, name='update_helper'),
    path('helper_dashboard/',
         views.helperDashboardView, name='helper_dashboard'),
    path('reviews/', views.helperReviewsView, name='helper_reviews'),
    path('deactive/', views.helperDeactivateView, name='deactive'),

 
]
