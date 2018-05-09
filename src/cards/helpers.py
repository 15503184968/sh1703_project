# -*- encoding: utf-8 -*-

# python apps
import datetime
import json
import pdb

# django apps
from django.db import transaction

# our apps
from .models import CardStatus, CardOperateType, Card, CardInfo, CardHistory


def write_CardHistory(
        card, operator_type, money, data_old, data_new, other=None,
        ):
    ''' 写流水账

    :param card: 银行卡
    :type card: Card
    :param operator_type: 操作类型
    :type operator_type: CardOperateType or String
    :param money: 发生金额
    :type money: int
    :param data_old: 业务发生前的数据
    :type data_old: dict
    :param data_new: 业务发生后的数据
    :type data_new: dict
    :param other: 其它信息
    :type other: dict

    :return: None or Exception
    '''
    if isinstance(operator_type, CardOperateType):
        s_operator_type = operator_type.name
    elif isinstance(operator_type, str):
        s_operator_type = operator_type
    else:
        msg = '操作类型错误. operator_type: {}'.format(operator_type)
        raise ValueError(msg)

    info = {
        '时间': datetime.datetime.now().isoformat(),
        '业务类型': s_operator_type,
        '发生金额': money,
        '业务发生前的数据': data_old,
        '业务发生后的数据': data_new,
    }
    if other:
        info['其它'] = other
    remark = json.dumps(info, ensure_ascii=False, indent=4)
    obj = CardHistory(
        card=card,
        operator_type=operator_type,
        remark=remark,
    )
    obj.save()


def write_CardHistory_2(card, operator_type, info):
    ''' 写流水账

    :param card: 银行卡
    :type card: Card
    :param operator_type: 操作类型
    :type operator_type: CardOperateType
    :param info: 内容
    :type money: dict
    :return: None or Exception
    '''
    remark = json.dumps(info, ensure_ascii=False, indent=4)
    obj = CardHistory(
        card=card,
        operator_type=operator_type,
        remark=remark,
    )
    obj.save()


def put_money(card, money):
    ''' 存款

    :param card: 银行卡
    :type card: Card
    :param money: 金额
    :type money: int
    :return: None or ValueError
    '''
    s_operator_type = '存款'
    s_status = '正常'

    if card.status.name != s_status:
        msg = '银行卡状态错误'
        raise ValueError(msg)

    try:
        operator_type = CardOperateType.objects.get(name=s_operator_type)
    except CardOperateType.DoesNotExist:
        msg = '银行卡操作类型不存在'
        raise ValueError(msg)

    old_autocommit = transaction.get_autocommit()
    try:
        # 关闭django的自动事务处理
        transaction.set_autocommit(False)

        # 前余额
        data_old = card.to_json()
        # 存款
        card.balance += money
        card.balance_available += money
        card.save()
        # 后余额
        data_new = card.to_json()
        # 写流水帐
        # info = {
        #     '时间': datetime.datetime.now().isoformat(),
        #     '业务类型': s_operator_type,
        #     '发生金额': money,
        #     '业务发生前的数据': data_old,
        #     '业务发生后的数据': data_new,
        # }
        # write_CardHistory(card, operator_type, info)
        write_CardHistory(card, operator_type, money, data_old, data_new,)

        # 事务提交
        transaction.commit()
    except Exception as e:
        msg = '未知错误. e: {}'.format(e)
        # 事务回滚
        transaction.rollback()
        raise ValueError(msg)
    finally:
        # 恢复django的自动事务处理
        transaction.set_autocommit(old_autocommit)


def get_money(card, money):
    ''' 取款

    :param card: 银行卡
    :type card: Card
    :param money: 金额
    :type money: int
    :return: None or ValueError
    '''
    pass
    s_operator_type = '取款'
    s_status = '正常'

    if card.status.name != s_status:
        msg = '银行卡状态错误'
        raise ValueError(msg)

    try:
        operator_type = CardOperateType.objects.get(name=s_operator_type)
    except CardOperateType.DoesNotExist:
        msg = '银行卡操作类型不存在'
        raise ValueError(msg)

    old_autocommit = transaction.get_autocommit()
    try:
        # 关闭django的自动事务处理
        transaction.set_autocommit(False)

        # 前余额
        data_old = card.to_json()
        # 检查余额
        if card.balance < money:
            msg = '余额不足'
            raise ValueError(msg)
        # 取款
        card.balance -= money
        card.balance_available -= money
        card.save()
        # 后余额
        data_new = card.to_json()
        # 写流水帐
        # info = {
        #     '时间': datetime.datetime.now().isoformat(),
        #     '业务类型': s_operator_type,
        #     '发生金额': money,
        #     '业务发生前的数据': data_old,
        #     '业务发生后的数据': data_new,
        # }
        # write_CardHistory(card, operator_type, info)
        write_CardHistory(card, operator_type, money, data_old, data_new,)

        # 事务提交
        transaction.commit()
    except Exception as e:
        msg = '未知错误. e: {}'.format(e)
        # 事务回滚
        transaction.rollback()
        raise ValueError(msg)
    finally:
        # 恢复django的自动事务处理
        transaction.set_autocommit(old_autocommit)


def credit_transfer(card_from, card_to, money):
    ''' 转账

    :param card_from: 转出银行卡
    :type card_from: Card
    :param card_to: 转入银行卡
    :type card_to: Card
    :param money: 金额
    :type money: int
    :return: None or ValueError
    '''
    s_operator_type = '转账'
    s_status = '正常'

    if card_from.status.name != s_status:
        msg = '转出银行卡状态错误'
        raise ValueError(msg)
    elif card_to.status.name != s_status:
        msg = '转入银行卡状态错误'
        raise ValueError(msg)

    try:
        operator_type = CardOperateType.objects.get(name=s_operator_type)
    except CardOperateType.DoesNotExist:
        msg = '银行卡操作类型不存在'
        raise ValueError(msg)

    old_autocommit = transaction.get_autocommit()
    try:
        # 关闭django的自动事务处理
        transaction.set_autocommit(False)

        ''' 转出 '''
        # 前余额
        data_from_old = card_from.to_json()
        # 检查余额
        if card_from.balance < money:
            msg = '余额不足'
            raise ValueError(msg)
        # 取款
        card_from.balance -= money
        card_from.balance_available -= money
        card_from.save()
        # 后余额
        data_from_new = card_from.to_json()
        # 写流水帐
        # info = {
        #     '时间': datetime.datetime.now().isoformat(),
        #     '业务类型': '{}-出'.format(s_operator_type),
        #     '发生金额': money,
        #     '业务发生前的数据': data_from_old,
        #     '业务发生后的数据': data_from_new,
        #     '转入银行卡': card_to.id,
        # }
        # write_CardHistory(card_from, operator_type, info)
        write_CardHistory(
                card_from, operator_type, money, data_from_old, data_from_old,
                {'转入银行卡号': card_to.id},
                )

        ''' 转入 '''
        # 前余额
        data_to_old = card_to.to_json()
        # 存款
        card_to.balance += money
        card_to.balance_available += money
        card_to.save()
        # 后余额
        data_to_new = card_to.to_json()
        # 写流水帐
        # info = {
        #     '时间': datetime.datetime.now().isoformat(),
        #     '业务类型': '{}-入'.format(s_operator_type),
        #     '发生金额': money,
        #     '业务发生前的数据': data_to_old,
        #     '业务发生后的数据': data_to_new,
        #     '转出银行卡': card_from.id,
        # }
        # write_CardHistory(card_to, operator_type, info)
        write_CardHistory(
                card_to, operator_type, money, data_to_old, data_to_old,
                {'转出银行卡号': card_from.id},
                )

        # 事务提交
        transaction.commit()
    except Exception as e:
        msg = '未知错误. e: {}'.format(e)
        # 事务回滚
        transaction.rollback()
        raise ValueError(msg)
    finally:
        # 恢复django的自动事务处理
        transaction.set_autocommit(old_autocommit)


def reversal(card, money):
    ''' 冲正

    :param card: 银行卡
    :type card: Card
    :param money: 金额
    :type money: int
    :return: None or ValueError
    '''
    s_operator_type = '冲正'

    try:
        operator_type = CardOperateType.objects.get(name=s_operator_type)
    except CardOperateType.DoesNotExist:
        msg = '银行卡操作类型不存在'
        raise ValueError(msg)

    old_autocommit = transaction.get_autocommit()
    try:
        # 关闭django的自动事务处理
        transaction.set_autocommit(False)

        # 前余额
        data_old = card.to_json()
        # 存款
        card.balance += money
        card.balance_available += money
        card.save()
        # 后余额
        data_new = card.to_json()
        write_CardHistory(card, operator_type, money, data_old, data_new)

        # 事务提交
        transaction.commit()
    except Exception as e:
        msg = '未知错误. e: {}'.format(e)
        # 事务回滚
        transaction.rollback()
        raise ValueError(msg)
    finally:
        # 恢复django的自动事务处理
        transaction.set_autocommit(old_autocommit)


