from .constants import CustomerVolume, JobExecutionSpeed
from kombu import Queue, Exchange


def get_celery_queues():
    queues = []
    count = 0
    for customer_type in CustomerVolume:
        for job_speed in JobExecutionSpeed:
            count+=1
            queue_name = "{}_{}".format(customer_type.value, job_speed.value)
            queues.append(Queue(queue_name, Exchange(queue_name), routing_key=queue_name))
    return queues