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
        # print('PutMoneyTestCase.setUp(): ...')

        models.Card.objects.get_or_create(id=1, status_id=1)
        models.Card.objects.get_or_create(id=2, status_id=1)
        models.CardInfo.objects.get_or_create(id=1, name='张三', card_id=1)
        models.CardInfo.objects.get_or_create(id=2, name='李四', card_id=2)

    def setUp_v1(self):
        ''' 初始化测试环境 '''
        # print('PutMoneyTestCase.setUp_v1(): ...')
        pass

        arr = [
            models.Card(status_id=1),
            models.Card(status_id=1),
        ]
        models.Card.objects.bulk_create(arr)

        arr = [
            models.CardInfo(name='张三', card_id=1),
            models.CardInfo(name='李四', card_id=2),
        ]
        models.CardInfo.objects.bulk_create(arr)

    def tearDown(self):
        ''' 释放测试环境 '''
        # print('PutMoneyTestCase.tearDown(): ...')
        pass

    def test_put_money_v3(self):
        ''' 存款 '''
        # print('PutMoneyTestCase.test_put_money_v3(): ...')

        o_id = 1
        money = 100

        c01 = models.Card.objects.get(pk=o_id)
        # print('test_put_money_v3 --> c01.balance: {}'.format(c01.balance))

        # 存款
        helpers.put_money_v3(c01, money)

        # 检查
        self.assertEqual(c01.balance, money, '余额错误')

        n = models.CardHistory.objects.filter(card_id=o_id).count()
        self.assertEqual(n, 1, '流水帐记录数量错误')
        # print('test_put_money_v3 --> c01.balance: {}'.format(c01.balance))

    def test_get_money_v2(self):
        ''' 取款 '''
        # print('PutMoneyTestCase.test_get_money_v2(): ...')

        o_id = 1
        money = 100

        c01 = models.Card.objects.get(pk=o_id)
        # print('test_get_money_v2 --> c01.balance: {}, 初始化'.format(c01.balance))
        # 存款
        helpers.put_money_v3(c01, money * 2)
        # print('test_get_money_v2 --> c01.balance: {}, 存钱200'.format(c01.balance))

        # 取款
        helpers.get_money_v2(c01, money)
        # print('test_get_money_v2 --> c01.balance: {}, 取款100'.format(c01.balance))

        # 检查
        self.assertEqual(c01.balance, money, '余额错误')

    def test_credit_transfer_v4(self):
        ''' 转账 '''
        o_id_from = 1
        o_id_to = 2
        money = 100

        c_from = models.Card.objects.get(pk=o_id_from)
        c_to = models.Card.objects.get(pk=o_id_to)
        # 存款
        helpers.put_money_v3(c_from, money)

        # 转账
        helpers.credit_transfer_v4(c_from, c_to, money)

        # 检查
        self.assertEqual(c_from.balance, 0, '余额错误')
        self.assertEqual(c_to.balance, money, '余额错误')

