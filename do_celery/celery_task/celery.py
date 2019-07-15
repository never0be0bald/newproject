from celery import Celery
from celery.schedules import crontab


broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/1'

# 生成celery对象
app = Celery('task', broker=broker, backend=backend, include=[
    'celery_task.add_task',
    'celery_task.send_email'
])


app.conf.beat_schedule = {
    # 'add-every-5-seconds': {
    #     'task': 'celery_task.add_task.add',
    #     'schedule': timedelta(seconds=10),
    #     'args': (1, 2)
    # },
    'add-every-10-seconds': {
        'task': 'celery_task.add_task.add',
        'schedule': crontab(minute=42),  # 不传的参数默认就是每的意思
        'args': (1, 2)
    }
}
# @app.task
# def add(x, y):
#     return x+y
#
#
# print(add.delay(1, 2))
