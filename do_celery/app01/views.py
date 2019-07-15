from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import json
# Create your views here.
from celery_task.add_task import add
from celery_task.send_email import send_email1


def index(request):
    ret = add.delay(1, 2)
    return HttpResponse(ret.id)


def register(request):
    if request.method == 'POST':
        dic = json.loads(request.body.decode('utf-8'))
        name = dic.get('name')
        password = dic.get('password')
        email = dic.get('email')
        user_obj = models.UserInfo.objects.filter(name=name).first()
        if user_obj:
            return HttpResponse('用户已存在')
        user_obj = models.UserInfo.objects.create(name=name, password=password, email=email)
        send_email1.delay(user_obj.id)
        return HttpResponse('注册成功，已向你发送一封激活邮件')
    return HttpResponse('ok')


def active_user(request):
    id = request.GET.get('id')
    models.UserInfo.objects.filter(id=id).update(is_active=1)
    return redirect('/login/')


def login(request):
    dic = json.loads(request.body.decode('utf-8'))
    name = dic.get('name')
    password = dic.get('password')
    user_obj = models.UserInfo.objects.filter(name=name, password=password).first()
    if not user_obj:
        return HttpResponse('用户不存在')
    if user_obj.is_active():
        return HttpResponse('登陆成功')
    return HttpResponse('OK')
