#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
from klineyes.markets.cache import read_cache

'''
A tushare wrapper

'''


class KlineData:

    def __init__(self):
        pass

    @read_cache
    def get_data(self, ktype='30', code='600496', start='2016-05-01', end='2016-06-09'):
        '''
        从缓存中读取股票数据
        :param ktype:
        :param code:
        :param start:
        :param end:
        :return:
        '''
        pass


kline_data = KlineData()

