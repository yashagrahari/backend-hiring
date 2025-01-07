from rest_framework import serializers
from .models import Site, UserRecords, Job, UserJobStatus, UserJobsDetails


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'domain', 'url', 'description', 'record_capicity']


class UserRecordsSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format="%Y-%m-%d", allow_null=True)
    class Meta:
        model = UserRecords
        fields = ['id', 'customer', 'site', 'name', 'email', 'phone', 'address', 'country', 'state', 'city', 'pincode', 'dob', 'is_active']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'name', 'execution_time', 'created_at', 'updated_at']


class UserJobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobStatus
        fields = ['id', 'status', 'started_at', 'completed_at', 'error_message']


class UserJobsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserJobsDetails
        fields = ['id', 'user', 'site', 'job', 'job_status', 'triggered_at']
