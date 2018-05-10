# -*- encoding: utf-8 -*-

# python apps
import datetime

# django apps
from django.db import transaction

# our apps
from .models import Card, CardHistory, CardOperateType


class NotAutoCommit:
    ''' 不使用django的自动提交 '''

    def __init__(self):
        print('NotAutoCommit.__init__(): ...')
        # 保存django自动事务的设置
        self.old_autocommit = transaction.get_autocommit()

    def __enter__(self):
        print('NotAutoCommit.__enter__(): ...')
        # 关闭django自动事务
        transaction.set_autocommit(False)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('NotAutoCommit.__exit__(): ...')
        # 恢复django自动事务的设置
        transaction.set_autocommit(self.old_autocommit)



def put_money(card, money):
    ''' 存款

    :param card: 银行卡
    :type card: Card
    :param money: 发生金额
    :type money: int
    :return: None or Exception
    '''
    pass
    s_status = '正常'
    s_operator_type = '存款'

    with NotAutoCommit():
        try:
            if card.status.name == s_status:
                try:
                    operator_type = CardOperateType.objects.get(name=s_operator_type)
                except CardOperateType.DoesNotExist:
                    msg = '操作类型不存在. operator_type: {}'.format(s_operator_type)
                    raise ValueError(msg)

                # 业务发生前的数据
                data_old = card.to_json()
                # 存钱
                card.balance += money
                card.balance_available += money
                card.save()
                # 业务发生后的数据
                data_new = card.to_json()
                # 写流水帐
                remark = '''
                时间：{now},
                发生金额：{money},
                业务发生前的数据：{data_old},
                业务发生后的数据：{data_new},
                '''.format(
                    now=datetime.datetime.now().isoformat(),
                    money=money,
                    data_old=data_old,
                    data_new=data_new,
                )

                # raise ValueError('调试')

                obj = CardHistory(
                    card=card,
                    operator_type=operator_type,
                    remark=remark,
                )
                obj.save()

                # 数据提交
                transaction.commit()
                print('数据提交!')
            else:
                msg = '银行卡的状态错误. status: {}'.format(card.status.name)
                raise ValueError(msg)
        except Exception as e:
            # 数据回滚
            msg = '未知错误. e: {}'.format(e)
            transaction.rollback()
            print(msg)



def put_money_2(card, money):
    ''' 存款

    :param card: 银行卡
    :type card: Card
    :param money: 发生金额
    :type money: int
    :return: None or Exception
    '''
    pass
    s_status = '正常'
    s_operator_type = '存款'

    # 保存django自动事务的设置
    old_autocommit = transaction.get_autocommit()
    try:
        # 关闭django自动事务
        transaction.set_autocommit(False)

        if card.status.name == s_status:
            try:
                operator_type = CardOperateType.objects.get(name=s_operator_type)
            except CardOperateType.DoesNotExist:
                msg = '操作类型不存在. operator_type: {}'.format(s_operator_type)
                raise ValueError(msg)

            # 业务发生前的数据
            data_old = card.to_json()
            # 存钱
            card.balance += money
            card.balance_available += money
            card.save()
            # 业务发生后的数据
            data_new = card.to_json()
            # 写流水帐
            remark = '''
            时间：{now},
            发生金额：{money},
            业务发生前的数据：{data_old},
            业务发生后的数据：{data_new},
            '''.format(
                now=datetime.datetime.now().isoformat(),
                money=money,
                data_old=data_old,
                data_new=data_new,
            )

            # raise ValueError('调试')

            obj = CardHistory(
                card=card,
                operator_type=operator_type,
                remark=remark,
            )
            obj.save()

            # 数据提交
            transaction.commit()
            print('数据提交!')
        else:
            msg = '银行卡的状态错误. status: {}'.format(card.status.name)
            raise ValueError(msg)
    except Exception as e:
        # 数据回滚
        msg = '未知错误. e: {}'.format(e)
        transaction.rollback()
        print(msg)
    finally:
        # 恢复django自动事务的设置
        transaction.set_autocommit(old_autocommit)
        print('恢复django自动设置的设置')

