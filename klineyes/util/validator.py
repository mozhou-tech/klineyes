#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
from klineyes.exception import ValidatorError

'''
共用函数工具包
'''

def data_validator(input_data):
    '''
    Data Validator
    :param input_data:
    :return:
    '''
    columns = ['ticker', 'tradeDate', 'turnoverVol', 'closePrice', 'highestPrice', 'lowestPrice', 'openPrice', 'preClosePrice']
    if type(input_data) == np.ndarray:
        if isinstance(input_data, np.ndarray) is False:
            raise ValidatorError('err data type.')
        if len(input_data[0]) < 8:
            raise ValidatorError('input array matrix at least 8 columns.')
        return pd.DataFrame(input_data, columns=columns)
    elif type(input_data) == pd.core.frame.DataFrame:
        for col in columns:    # 验证columns是否期权
            if any(col == column_list for column_list in input_data.columns) is False:
                raise ValidatorError('need column ' + col+'')
        return input_data
    else:
        raise ValidatorError('unsupported dtype.')


