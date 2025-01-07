import logging
from time import sleep
from celery import Task
from .models import UserJobStatus, UserJobsDetails, Job, Site
from datetime import datetime
from typing import Any
from vanderval.celery import app



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class BaseTaskWithTracking(Task):
    def on_success(self, retval, task_id, args, kwargs):
        job_status = UserJobStatus.objects.get(id=kwargs.get('job_status_id'))
        job_status.status = 'COMPLETED'
        job_status.completed_at = datetime.now()
        job_status.save()
        super().on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        job_status = UserJobStatus.objects.get(id=kwargs.get('job_status_id'))
        job_status.status = 'FAILED'
        job_status.completed_at = datetime.now()
        job_status.error_message = str(exc)
        job_status.save()
        super().on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=BaseTaskWithTracking, bind=True)
def execute_task(self, task_number: int, job_details_id:int, **kwargs: Any) -> bool:
    task_mapping = {
        1: task_01,
        2: task_02,
        3: task_03,
        4: task_04,
        5: task_05
    }
    
    return task_mapping[task_number](job_details_id)


def task_01(job_details_id: int):
    # TIME_MULTIPLIER = 0.001 # very fast execution per record
    # site = Site.objects.get(id=site_id)
    # record = UserJobsDetails.objects.filter(site=site, user_id= user_id)
    # for record in records:
    #     sleep(TIME_MULTIPLIER)
    record = UserJobsDetails.objects.get(id= job_details_id)
    logger.info("Task 01: {} processed by {}".format(record.job.name, record.user.username))
    return True


def task_02(job_details_id: int):
    # TIME_MULTIPLIER = 0.01
    # site = Site.objects.get(id=site_id)
    # record = UserJobsDetails.objects.filter(site=site, user_id= user_id)
    # for record in records:
    #     sleep(TIME_MULTIPLIER)
    record = UserJobsDetails.objects.get(id= job_details_id)
    logger.info("Task 02: {} processed by {}".format(record.job.name, record.user.username))
    return True


def task_03(job_details_id: int):
    # TIME_MULTIPLIER = 0.1
    # site = Site.objects.get(id=site_id)
    # record = UserJobsDetails.objects.filter(site=site, user_id= user_id)
    record = UserJobsDetails.objects.get(id= job_details_id)
    logger.info("Task 03: {} processed by {}".format(record.job.name, record.user.username))
    return True


def task_04(job_details_id: int):
    # TIME_MULTIPLIER = 1
    # site = Site.objects.get(id=site_id)
    # record = UserJobsDetails.objects.filter(site=site, user_id= user_id)
    # for record in records:
    #     sleep(TIME_MULTIPLIER)
    record = UserJobsDetails.objects.get(id= job_details_id)
    logger.info("Task 04: {} processed by {}".format(record.job.name, record.user.username))
    return True


def task_05(job_details_id: int):
    # TIME_MULTIPLIER = 10
    # site = Site.objects.get(id=site_id)
    record = UserJobsDetails.objects.get(id= job_details_id)
    # for record in records:
    #     sleep(TIME_MULTIPLIER)
    logger.info("Task 05: {} processed by {}".format(record.job.name, record.user.username))
    return True
