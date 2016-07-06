#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime as dt

from klineyes.util.show_plot import mfi as show_plot_mfi
from klineyes.util.show_plot import atr as show_plot_atr
from klineyes.util.show_plot import rocr as show_plot_rocr

from klineyes.markets.stocks.kline_data import kline_data

# print kline_data.get_basic_data(ktype='30', code='000001', start='2016-04-11', end='2016-06-12')
# 300181 300121
df = kline_data.get_indicator(ktype='D', code='sz', start='2013-01-01', end='2016-07-07', indicator=['MFI', 'ROCR','ATR'])

# print df

# show_plot_rocr(df)
# show_plot_mfi(df)
show_plot_atr(df)





