#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
import exception

'''
共用函数工具包
'''

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # project root path


def data_validator(input_data):
    '''
    Data Validator
    :param input_data:
    :return:
    '''
    columns = ['ticker', 'tradeDate', 'turnoverVol', 'closePrice', 'highestPrice', 'lowestPrice', 'openPrice', 'preClosePrice']
    if type(input_data) == np.ndarray:
        if isinstance(input_data, np.ndarray) is False:
            raise exception.ValidatorError('err data type.')
        if len(input_data[0]) < 8:
            raise exception.ValidatorError('input array matrix at least 8 columns.')
        return pd.DataFrame(input_data, columns=columns)
    elif type(input_data) == pd.core.frame.DataFrame:
        for col in columns:    # 验证columns是否期权
            if any(col == column_list for column_list in input_data.columns) is False:
                raise exception.ValidatorError('need column ' + col+'')
        return input_data
    else:
        raise exception.ValidatorError('unsupported dtype.')

def load_test_data(ticker='000001'):
    '''
    Load test test_data for develop
    :param ticker:
    :return: 	ticker	tradeDate	turnoverVol	closePrice	highestPrice	lowestPrice	openPrice
    '''
    return pd.read_csv(BASE_DIR+'/tests/test_data/'+ticker+'.csv', dtype={"ticker": np.str}, index_col=0)