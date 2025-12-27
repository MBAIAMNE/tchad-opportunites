from django.urls import path
from . import views

urlpatterns = [
    path('emplois/', views.job_list, name='job_list'),
    path('emplois/<int:pk>/', views.job_detail, name='job_detail'),
    path('emplois/<int:pk>/postuler/', views.apply_job, name='apply_job'),
    
    path('opportunites/', views.opportunity_list, name='opportunity_list'),
    path('opportunites/<int:pk>/', views.opportunity_detail, name='opportunity_detail'),
]