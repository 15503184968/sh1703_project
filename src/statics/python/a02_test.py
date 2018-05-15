# -*- encoding: utf-8 -*-

# python apps
from browser import document, alert


def echo(ev):
    ''' 弹出窗口 '''
    print('a02_test.py --> echo(): ...')
    alert(document['zone'].value)


document['mybutton'].bind('click', echo)
