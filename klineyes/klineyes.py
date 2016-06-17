#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

from .util.validator import data_validator
from .classifier import candlestick_single
from .classifier import candlestick_multi

'''
主要模块
'''
ret_func = lambda x: None if x.empty else x.set_index('tradeDate')


def get_dates_pattern(input_data, ptypes = None):
    '''
    获取某些日期的特征图形,每个交易日单独判断
    :param input_data: DataFrame
    :param ptypes: pattern 类型 ['hammer', 'line', 'star']
    :return:
    '''
    result_holder = None
    df = data_validator(input_data)
    if ptypes['single']:  # 处理单日情况
        ret_dict = []
        for i, row in df.iterrows():
            feature = candlestick_single.classifier_single_date(row, ptypes=ptypes['single'])
            if feature is not None:
                ret_dict.append({'tradeDate': row.tradeDate, 'pattern': feature})
        result_holder = ret_func(pd.DataFrame(ret_dict))
    if ptypes['multi']:   # 处理多日情况
        for ptype in ptypes['multi']:
            ret_dict = []
            for i, row in df[::-1].iterrows():
                data_cell = df[i-1:i+1] if ptype == 'multi_double' else None
                data_cell = df[i-2:i+1] if data_cell is None and ptype == 'triple_fivefold' else data_cell
                data_cell = df[i-4:i+1] if data_cell is None and ptype == 'multi_fivefold' else data_cell
                feature = candlestick_multi.classifier_multi_date(data_cell, ptype=ptype)
                if feature is not None:
                    ret_dict.append({'tradeDate': row.tradeDate, 'pattern': feature})
            if type(result_holder) == pd.core.frame.DataFrame:
                result_holder = result_holder.append(ret_func(pd.DataFrame(ret_dict)))
            else:
                result_holder = ret_func(pd.DataFrame(ret_dict))
    return result_holder


def custom_judge():
    pass
