# -*- encoding: utf-8 -*-

# python apps

# django apps
from rest_framework import serializers

# our apps
from .models import Card, CardInfo


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id', 'balance', 'balance_available', 'balance_freeze', 'status_id',
        )



class PutMoneySerializer(serializers.Serializer):
    ''' 存钱 '''

    card_id = serializers.IntegerField()
    money = serializers.IntegerField()

    def validate_money(self, money):
        ''' 存钱的金额，必须大于0

        :param money: 金额
        :return: int or ValidationError
        '''
        print('PutMoneySerializer.validate_money(): ...')
        print('\ttype(money): {}'.format(type(money)))
        if 0 < money:
            ret = money
            print('ret: {}'.format(ret))
            return ret
        else:
            msg = '存钱的金额，必须大于0'
            raise serializers.ValidationError(msg)

    def validate(self, data):
        print('PutMoneySerializer.validate(): ...')
        print('\tdata: {}'.format(data))

        return data
