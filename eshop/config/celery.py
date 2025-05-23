import os
from celery import Celery
from kombu import Exchange, Queue
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY') #from django.conf import settings

# تنظیمات مربوط به rabbitmq

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

# تنظیمات مربوط به rabbitmq

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

# @app.task(queue='tasks')
# def send_message(mobile, message):
#     time.sleep(3)
#     return f'sms sends to user with {mobile} number and message was: {message}'



# app.conf.task_routes = {
#     'notifications.tasks.send_discount_emails' : {'queue' : 'queue1'},
#     'notifications.tasks.process_data_for_ml' : {'queue' : 'queue2'},
# }

# app.conf.task_default_rate_limit = '1/m'

# تنظیمات redis

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }

# queues => celery,celery:1,celery:2,celery:3

app.autodiscover_tasks()