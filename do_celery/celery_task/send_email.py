import os
import sys

if __name__ == "celery_task.send_email":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "do_celery.settings")
    import django
    django.setup()
    from celery_task.celery import app
    from app01 import models
    from django.core.mail import send_mail
    import threading
    from do_celery import settings


    @app.task
    def send_email1(id):
        user_obj = models.UserInfo.objects.filter(pk=id).first()
        email = user_obj.email
        t = threading.Thread(target=send_mail, args=(
            "激活邮件，点击激活账号",
            '点击该邮件激活你的账号，否则无法登陆',
            settings.EMAIL_HOST_USER,
            [email],
            ),
            kwargs={'html_message': "<a href='http://127.0.0.1:8000/active_user/?id=%s'>点击激活gogogo</a>" % id}
        )
        t.start()
