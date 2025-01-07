from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Site, Job, UserJobsDetails, UserJobStatus
from .serializers import SiteSerializer, UserRecordsSerializer, JobSerializer, UserJobsDetailsSerializer
from .services import TaskScheduler
from datetime import date


class SiteListCreateAPIView(APIView):
    """
    API view to create and list sites
    """
    def get(self, request):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SiteDetailAPIView(APIView):
    """
    API view to get, update or delete site by ID
    """
    def get(self, request, site_id):
        try:
            site = Site.objects.get(id=site_id)
        except Site.DoesNotExist:
            return Response({"error": "Site not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SiteSerializer(site)
        return Response(serializer.data)

    def put(self, request, site_id):
        try:
            site = Site.objects.get(id=site_id)
        except Site.DoesNotExist:
            return Response({"error": "Site not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, site_id):
        try:
            site = Site.objects.get(id=site_id)
        except Site.DoesNotExist:
            return Response({"error": "Site not found"}, status=status.HTTP_404_NOT_FOUND)

        site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRecordsCreateAPIView(APIView):
    """
    API view to create user record for a specific user and site
    """
    def post(self, request):
        try:
            data = (request.data)
            site = Site.objects.get(id=data['site'])
            user = User.objects.get(id=data['customer'])
        except (Site.DoesNotExist, User.DoesNotExist):
            return Response({"error": "User or Site not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRecordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobListCreateAPIView(APIView):
    """
    API view to create and list jobs
    """
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):
    """
    API view to get, update or delete job by ID
    """
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        return Response(serializer.data)

    def put(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserJobsDetailsListAPIView(APIView):
    """
    API view to list user job details
    """
    def get(self, request):
        user_jobs_details = UserJobsDetails.objects.all()
        serializer = UserJobsDetailsSerializer(user_jobs_details, many=True)
        return Response(serializer.data)
    

class UserJobsDetailsAPIView(APIView):
    """
    API view to get user job details by ID
    """
    def get(self, request, user_job_detail_id):
        try:
            user_job_detail = UserJobsDetails.objects.get(id=user_job_detail_id)
        except UserJobsDetails.DoesNotExist:
            return Response({"error": "User job detail not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserJobsDetailsSerializer(user_job_detail)
        return Response(serializer.data)
    


class TriggerJobApiView(APIView):
    """
    API view to schedule task
    """
    def post(self, request):
        user_id = request.data.get('user_id') # we can get from login session if it is implemented
        site_id = request.data.get('site_id')
        job_id = request.data.get('job_id')
        
        job_status_id = TaskScheduler.schedule_task(user_id, site_id, job_id)
        return Response({'job_status_id': job_status_id})
    
    def get(self, request, job_status_id):
        status = UserJobStatus.objects.get(id=job_status_id)
        return Response({
            'status': status.status,
            'started_at': status.started_at,
            'completed_at': status.completed_at,
            'error_message': status.error_message
        })
