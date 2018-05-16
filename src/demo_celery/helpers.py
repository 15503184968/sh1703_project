# -*- encoding: utf-8 -*-

# python apps
import datetime
import uuid

# our apps
from .models import Todo


def todo_create(title, remark=None):
    ''' 创建Todo记录

    :param title: 标题
    :type title: str
    :param remark: 备注
    :type remark: str or None
    :return: Todo实例 or Exception
    '''
    obj = Todo(title=title)
    if remark is not None:
        obj.remark = remark
    obj.remark += '\n\nnow: {}, 记录创建！'.format(
        datetime.datetime.now().isoformat(),
    )
    obj.save()
    return obj


def todo_process(todo):
    ''' 任务的处理过程

    :param todo: Todo实例
    :type todo: Todo
    :return: None or Exception
    '''
    if todo.status != 0:
        msg = '记录的状态错误.  status: {}'.format(todo.status)
        raise ValueError(msg)

    try:
        # 修改状态: 处理中
        todo.status = 1
        todo.save()

        # 执行业务逻辑
        obj = uuid.uuid4()
        todo.remark += '\n\nnow: {}, obj: {}'.format(
            datetime.datetime.now().isoformat(), obj.hex,
        )
        todo.save()

        # 修改状态: 处理完成
        todo.status = 2
        todo.save()
    except Exception as e:
        msg = '未知错误. e: {}'.format(e)

        # 修改状态: 错误
        todo.status = 3
        todo.save()

        raise ValueError(msg)

