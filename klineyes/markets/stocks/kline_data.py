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
    def minutes(self, ktype='30', code='600496', start='2016-05-01', end='2016-06-09'):
        # return ts.get_hist_data(code=code, ktype=period, start=start, end=end)
        pass


kline_data = KlineData()

