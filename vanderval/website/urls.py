from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.SiteListCreateAPIView.as_view(), name='create_list_sites'),
    path('site/<int:site_id>/', views.SiteDetailAPIView.as_view(), name='get_site'),

    path('user-records/', views.UserRecordsCreateAPIView.as_view(), name='create_user_record'),

    path('jobs/', views.JobListCreateAPIView.as_view(), name='create_list_jobs'),
    path('job/<int:job_id>/', views.JobDetailAPIView.as_view(), name='get_job'),

    path('user-job-details/', views.UserJobsDetailsListAPIView.as_view(), name='create_list_user_jobs_details'),
    path('trigger-job/', views.TriggerJobApiView.as_view(), name='trigger-job'),
    path('trigger-job-detail/<str:job_status_id>', views.GetJobStatus.as_view(), name='trigger-job-detail')
]
