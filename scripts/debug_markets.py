#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.markets.stocks.kline_data import kline_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# print kline_data.get_basic_data(ktype='30', code='000001', start='2016-04-11', end='2016-06-12')
df = kline_data.get_indicator(ktype='30', code='300181', start='2016-04-01', end='2016-06-13', indicator=['MACD'])
# print df[df.macdhist == df[df.macd_shape == 'golden'].macdhist.min()]
golden = df[df.macd_shape == 'golden']
death = df[df.macd_shape == 'death']
inc_touch_zero = df[df.macd_shape == 'inc_touch_zero']
negative_macd_median = df[df.macddif < 0.].macddif.median()   # macd 的中位数
positive_macd_median = df[df.macddif > 0.].macddif.median()   # macd 的中位数

for i, row in golden.iterrows():
    if row.macddif < negative_macd_median:
        print 'negative'
        print row.date
    elif row.macddif > positive_macd_median:
        print 'positive' + str(row.macddif)
        print row.date













def show_plot():

    df['date'] = pd.to_datetime(df.date)
    # 绘图
    fig = plt.figure(figsize=(16, 9))
    gs = GridSpec(3, 1) # 2 rows, 3 columns

    price = fig.add_subplot(gs[:2, 0])
    price.plot(df['date'], df['close'], color='blue')

    indicator = fig.add_subplot(gs[2, 0], sharex=price)
    indicator.plot(df['date'], df['macdsignal'], c='pink')
    indicator.plot(df['date'], df['macd'], c='yellowgreen')
    indicator.plot(df['date'], [0.]*len(df['date']), c='gray')
    # indicator.bar(df['date'],df['macdhist'])#df['macdhist']
    # 划MACD交点
    area = np.pi * 5  # 0 to 15 point radiuses
    indicator.scatter(golden['date'].values, golden['macd'].values,s = area, color='red')
    indicator.scatter(death['date'].values, death['macd'].values,s = area, color='green')
    price.scatter(golden['date'].values, golden['close'].values,s = area, color='red')
    price.scatter(death['date'].values, death['close'].values,s = area, color='green')
    price.grid(True)
    indicator.grid(True)
    plt.tight_layout()
    plt.show()

# show_plot()