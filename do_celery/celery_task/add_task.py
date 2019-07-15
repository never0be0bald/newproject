from celery_task.celery import app


@app.task
def add(x, y):
    return x+y
