#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.markets.stocks.kline_data import kline_data


# print kline_data.get_basic_data(ktype='30', code='000001', start='2016-04-11', end='2016-06-12')
print kline_data.get_indicator(ktype='30', code='300181', start='2016-04-01', end='2016-06-12',indicator=['MACD','MFI'])



