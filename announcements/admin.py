from django.contrib import admin
from .models import Job, Opportunity

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'city', 'deadline', 'created_at')
    search_fields = ('title', 'organization')

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'type_opp', 'organization', 'deadline', 'created_at')
    search_fields = ('title', 'organization')