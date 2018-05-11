# -*- encoding: utf-8 -*-

# django apps
from django.test import TestCase

# our apps
from . import models, helpers


class PutMoneyTestCase(TestCase):
    ''' 存钱 '''

    fixtures = ['initial_data.json', ]

    def setUp(self):
        ''' 初始化测试环境 '''
        pass

        c01 = models.Card(status_id=1)
        c01.save()
        print('c01.id: {}'.format(c01.id))
        c02 = models.Card(status_id=1)
        c02.save()
        # self.arr_Card = [c01, c02]
        # models.CardInfo.objects.bulk_create(self.arr_Card)

        c01_info = models.CardInfo(name='张三', card_id=c01.id)
        # c01_info.save()
        c02_info = models.CardInfo(name='李四', card_id=c02.id)
        # c02_info.save()
        arr = [c01_info, c02_info]
        models.CardInfo.objects.bulk_create(arr)
        print('c01_info.id: {}'.format(c01_info.id))

    def tearDown(self):
        ''' 释放测试环境 '''
        pass

    def test_right(self):
        ''' 正确的情况 '''
        c01 = models.Card.objects.get(pk=1)
        money = 100
        helpers.put_money(c01, money)

        c01 = models.Card.objects.get(pk=1)
        self.assertEqual(c01.balance, money)


