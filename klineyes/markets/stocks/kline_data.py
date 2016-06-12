#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
from klineyes.markets.cache import read_cache
import talib as ta
import pandas as pd

'''
A tushare wrapper

'''
INDICATOR = ['MACD', 'MFI']

class KlineData:

    def __init__(self):
        pass

    @read_cache
    def get_basic_data(df):
        '''
        从缓存中读取股票数据
        :param ktype:
        :param code:
        :param start:
        :param end:
        :return:
        '''
        return df.ix[:, :'price_change']

    @read_cache
    def get_indicator(df, indicator):
        ret_df = None
        if 'MACD' in indicator:
            macd, macdsignal, macdhist = ta.MACD(df.close.values, fastperiod=12, slowperiod=26, signalperiod=9)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([macd, macdsignal, macdhist]).T.rename(columns={0: "MACD", 1: "MACDSIGNAL", 2: "MACDHIST"}), ret_df)
        if 'MFI' in indicator:
            real = ta.MFI(df.high.values, df.low.values, df.close.values, df.volume.values, timeperiod=14)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([real]).T.rename(columns={0: "MFI"}), ret_df)
        return ret_df

    @staticmethod
    def _merge_dataframe(source, target):
        if target is None:
            target = source
        else:
            target = target.merge(source)
        return target

kline_data = KlineData()

