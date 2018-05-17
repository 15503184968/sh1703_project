# -*- encoding: utf-8 -*-
''' 参考:
http://www.cnblogs.com/nanrou/p/7026789.html
'''
import os

# 调试模式
# debug = 'reload'
# 项目的ip地址:端口号
bind = '127.0.0.1:5051'
# 允许挂起的连接数
backlong = 1024
# 工作进程数量
workers = 3
# 工作进程使用的异步库
work_class = 'gevent'
# 重启之前的最大请求数(防止内存泄漏)
max_requests = 10240
# django启动目录
chdir = '/home/u01/src/work/sh1703/sh1703_project/src'
# 守护进程
# daemon = True
# 使用unix域套接字(Unix Domain Socket)
pidfile = '/home/u01/src/work/sh1703/sh1703_project/logs//sh1703_project.pid'
# 访问日志
accesslog = '/home/u01/src/work/sh1703/sh1703_project/logs/gunicorn/access.log'
# 错误日志
errorlog = '/home/u01/src/work/sh1703/sh1703_project/logs/gunicorn/error.log'
# 日志级别
loglevel = 'debug'
# 项目的进程名称
proc_name = 'sh1703_project'
# 项目的python环境
pythonpath = '/home/u01/src/work/sh1703/sh1703_project/src'

