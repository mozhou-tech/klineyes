#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import talib as ta

from klineyes.classifier.tools import line_intersections
from klineyes.markets.cache import read_cache

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
        ret_df = df
        if 'MACD' in indicator:
            macd, macdsignal, macdhist = ta.MACD(df.close.values, fastperiod=12, slowperiod=26, signalperiod=9)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([macd, macdsignal, macdhist]).T.rename(columns={0: "macddif", 1: "macddem", 2: "macdhist"}), ret_df)
            ret_df = KlineData._merge_dataframe(line_intersections(ret_df, columns=['macddif', 'macddem']), ret_df)
        if 'MFI' in indicator:
            real = ta.MFI(df.high.values, df.low.values, df.close.values, df.volume.values, timeperiod=14)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([real]).T.rename(columns={0: "mfi"}), ret_df)
        if 'ATR' in indicator:
            real = ta.ROC(df.high.values, df.low.values, df.close.values, timeperiod=14)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([real]).T.rename(columns={0: "atr"}), ret_df)
        if 'ROCR' in indicator:
            real = ta.ROCR(df.close.values, timeperiod=10)
            ret_df = KlineData._merge_dataframe(pd.DataFrame([real]).T.rename(columns={0: "rocr"}), ret_df)
        ret_df['date'] = pd.to_datetime(ret_df['date'], format='%Y-%m-%d')
        return ret_df

    @staticmethod
    def _merge_dataframe(source, target):
        '''
        合并DataFrame
        :param source:
        :param target:
        :return:
        '''
        if target is None:
            target = source
        else:
            target = pd.merge(target.reset_index(), source.reset_index(), on=None).drop('index', 1)
        return target

kline_data = KlineData()

