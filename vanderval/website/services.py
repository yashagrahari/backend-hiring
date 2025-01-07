from uuid import UUID
from .models import UserJobsDetails, UserJobStatus, Job, UserRecords
from .constants import CustomerVolume, JobExecutionSpeed
from .tasks import execute_task

class TaskScheduler:
    @staticmethod
    def get_queue_name(customer_id: int, job_id: int) -> str:
        customer_volume = UserRecords.get_customer_volume(customer_id)
        job = Job.objects.get(id=job_id)
        job_speed = job.get_job_type()
        return "{}_{}".format(customer_volume.value, job_speed.value)

    @staticmethod
    def schedule_task(user_id: int, site_id: int, job_id: int) -> UUID:
        job_status = UserJobStatus.objects.create(status='PENDING')
        
        job_details = UserJobsDetails.objects.create(
            user_id=user_id,
            site_id=site_id,
            job_id=job_id,
            job_status=job_status
        )

        queue_name = TaskScheduler.get_queue_name(user_id, job_id)
        print(queue_name)
        job = Job.objects.get(id=job_id)
        task_number = int(job.name.split('_')[1])  
        print(task_number)
        execute_task.apply_async(
            args=[task_number, site_id],
            kwargs={'job_status_id': str(job_status.id)},
            queue=queue_name
        )

        return job_status.id