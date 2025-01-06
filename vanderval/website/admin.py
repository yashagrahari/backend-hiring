from django.contrib import admin
from .models import Site, UserRecords, Job, UserJobStatus, UserJobsDetails

# Register the models here
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'record_capicity')
    search_fields = ('name', 'domain')

@admin.register(UserRecords)
class UserRecordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'site', 'is_active')
    search_fields = ('name', 'email')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'execution_time', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(UserJobStatus)
class UserJobStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'started_at', 'completed_at')
    search_fields = ('status',)

@admin.register(UserJobsDetails)
class UserJobsDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'site', 'job', 'job_status', 'triggered_at')
    search_fields = ('user__username', 'site__name', 'job__name')
