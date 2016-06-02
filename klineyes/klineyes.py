#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from .common import data_validator
from .classifier import single

'''
主要模块
'''
ret_func = lambda x: None if x.empty else x.set_index('tradeDate')


def get_dates_by_pattern(input_data, pattern):
    '''
    获取图形对应的日期
    :param input:
    :param pattern:
    :return:
    '''
    pass


def get_dates_pattern(input_data, ptypes = None):
    '''
    获取某些日期的特征图形,每个交易日单独判断
    :param input_data: DataFrame
    :param ptypes: pattern 类型 ['hammer', 'line', 'star']
    :return:
    '''
    df = data_validator(input_data)
    ret_dict = []
    for i, row in df.iterrows():
        feature = single.classifier_single_date(row, ptypes=ptypes)
        if feature is not None:
            ret_dict.append({'tradeDate': row.tradeDate, 'pattern': feature})
    return ret_func(pd.DataFrame(ret_dict))
