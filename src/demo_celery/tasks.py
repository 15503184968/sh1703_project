# -*- encoding: utf-8 -*-

# celery apps
from celery.task import task

# our apps
from .helpers import todo_create, todo_process
from .models import Todo


@task
def calc_01(todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo_process(todo)
    except ValueError as e:
        msg = str(e)
        print(msg)
    except Exception as e:
        msg = str(e)
        print(msg)
