#!/usr/bin/python
# -*- coding: UTF-8 -*-

import klineyes.markets.stocks.get_realtime as get_realtime
import tushare as ts
print ts.get_hist_data(code='600496', ktype='30').index



