#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec
from klineyes.util.show_plot import mfi as show_plot_mfi

from klineyes.markets.stocks.kline_data import kline_data

# print kline_data.get_basic_data(ktype='30', code='000001', start='2016-04-11', end='2016-06-12')
# 300181 300121
df = kline_data.get_indicator(ktype='60', code='sh', start='2016-03-01', end='2016-07-06', indicator=['MFI'])



show_plot_mfi(df)





