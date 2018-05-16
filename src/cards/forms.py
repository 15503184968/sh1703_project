# -*- encoding: utf-8 -*-

# python apps

# django apps
from django import forms

# our apps


class PutMoneyForm(forms.Form):
    card_id = forms.IntegerField(label='银行卡号')
    money = forms.IntegerField(label='发生金额')


class CeleryTestForm(forms.Form):
    ''' 测试celery '''
    title = forms.CharField(label='标题', max_length=128)
    remark = forms.CharField(label='备注', required=False)
