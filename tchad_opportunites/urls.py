from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('emplois/', core_views.job_list, name='job_list'),
    path('formations/', core_views.formation_list, name='formation_list'),
    path('stages/', core_views.stage_list, name='stage_list'),
    path('appels/', core_views.appel_list, name='appel_list'),
]
