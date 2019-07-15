from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "do_celery.settings")
    import django
    django.setup()
    print('this is a test')
    # class Foo(type):
    #     pass
    #     # def __init__(self):
    #     #     super(Foo, self).__init__()
    # obj1 = Foo('hello', (object,), {'a': 1})
    # print(obj1)
    # print(obj1())
    # import html
    # import threading
    #
    # def add(x, y, z=10):
    #     print(x, y, z)
    #     return x+y+z
    # result = threading.Thread(target=add, args=(5, 6), kwargs={'z': 7})
    # result.start()
    # from celery import Celery
    #
    # broker = 'redis://127.0.0.1:6379/0'
    # backend = 'redis://127.0.0.1:6379/1'
    #
    # # 生成celery对象
    # app = Celery('task', broker=broker, backend=backend, include=['celery_task.add_task'])

