from celery import shared_task
import time

# @shared_task(queue='celery')
# def task_1():
#     time.sleep(3)
#     return

@shared_task(queue='tasks')
def send_sms_to_user():
    time.sleep(6)
    print('sms has been sent to user.')