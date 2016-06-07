#!/usr/bin/python
# -*- coding: UTF-8 -*-

import klineyes.markets.stocks.get_realtime as get_realtime
import tushare as ts
print ts.get_hist_data(code='600496', start='2016-06-01', end='2016-06-09', ktype='30')



