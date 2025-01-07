import uuid
from django.db import models
from django.contrib.auth.models import User
from .constants import CustomerVolume, JobExecutionSpeed

# Create your models here.
class Site(models.Model):
    RECORD_CAPACITY_LOW = 1  # user records between 500-10000
    RECORD_CAPACITY_MEDIUM = 2  # user records between 10000-50000
    RECORD_CAPACITY_HIGH = 3  # user records between 50000-200000

    RECORD_CAPACITY_CHOICES = (
        (RECORD_CAPACITY_LOW, "Low"),
        (RECORD_CAPACITY_MEDIUM, "Medium"),
        (RECORD_CAPACITY_HIGH, "High"),
    )

    name = models.CharField(max_length=100)
    domain = models.URLField()
    url = models.URLField()
    description = models.TextField()
    record_capicity = models.IntegerField(choices=RECORD_CAPACITY_CHOICES)


class UserRecords(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    
    @staticmethod
    def get_customer_volume(customer_id):
        """
        Categorizes the customer based on the number of sites they're associated with.
        """
        site_count = UserRecords.objects.filter(customer_id=customer_id, is_active=True).values('site').distinct().count()

        if site_count <= 3:
            return CustomerVolume.HIGH
        elif 4 <= site_count <= 10:
            return CustomerVolume.MEDIUM
        else:
            return CustomerVolume.HIGH

    def __str__(self):
        return "{} ({})".format(self.name, self.email)
    
    class Meta:
        verbose_name_plural = "User Records"


class Job(models.Model):
    name = models.CharField(max_length=100)
    execution_time = models.FloatField(help_text="Execution time in seconds")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_job_type_by_execution_time(execution_time):
        """
        Fetch the job type category based on execution time.
        """
        if execution_time <= 120:
            return JobExecutionSpeed.VERY_SLOW
        elif execution_time <= 240:
            return JobExecutionSpeed.SLOW
        elif execution_time <= 360:
            return JobExecutionSpeed.MEDIUM
        elif execution_time <= 480:
            return JobExecutionSpeed.FAST
        else:
            return JobExecutionSpeed.VERY_FAST

    def get_job_type(self):
        """
        Get the job type for the current job instance based on its execution time.
        """
        return self.get_job_type_by_execution_time(self.execution_time)

    def __str__(self):
        return self.name

class UserJobStatus(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)
    
    class Meta:
        verbose_name_plural = "User Jobs Status"


class UserJobsDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    job_status = models.ForeignKey(UserJobStatus, on_delete=models.CASCADE)
    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {}, Job: {}, Site: {}".format(self.user.username, self.job.name, self.site.name)

    class Meta:
        verbose_name_plural = "User Jobs Details"

