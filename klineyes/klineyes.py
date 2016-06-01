#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from common import BASE_DIR
import classifier.single


def load_test_data(ticker='000001'):
    '''
    Load test test_data for develop
    :param ticker:
    :return: 	ticker	tradeDate	turnoverVol	closePrice	highestPrice	lowestPrice	openPrice
    '''
    df = pd.read_csv(BASE_DIR+'/tests/test_data/'+ticker+'.csv', dtype={"ticker": np.str}, index_col=0)
    # return np.array(df.values)
    return df


def data_validator(input_data):
    '''
    Data Validator
    :param input_data:
    :return:
    '''
    columns = ['ticker', 'tradeDate', 'turnoverVol', 'closePrice', 'highestPrice', 'lowestPrice', 'openPrice', 'preClosePrice']
    if type(input_data) == np.ndarray:
        if isinstance(input_data, np.ndarray) is False:
            raise Exception('err data type.')
        if len(input_data[0]) < 8:
            raise Exception('input array matrix at least 8 columns.')
        return pd.DataFrame(input_data, columns=columns)
    elif type(input_data) == pd.core.frame.DataFrame:
        for col in columns:    # 验证columns是否期权
            if any(col == column_list for column_list in input_data.columns) is False:
                raise Exception('need column ' + col+'')
        return input_data


def get_dates_by_pattern(input_data, pattern):
    '''
    获取图形对应的日期
    :param input:
    :param pattern:
    :return:
    '''
    input_data = load_test_data()
    df = data_validator(input_data)
    for i, row in df.iterrows():
        feature = classifier.single.classifier_single_date(row)
        if feature is not None:
            print row.tradeDate +' '+ feature


def get_dates_pattern(input_data):
    '''
    获取某些日期的特征图形
    :param input_data:
    :return:
    '''
    df = data_validator(input_data)
    ret_dict = []
    for i, row in df.iterrows():
        feature = classifier.single.classifier_single_date(row)
        if feature is not None:
            ret_dict.append({'tradeDate': row.tradeDate, 'pattern': feature})
    return pd.DataFrame(ret_dict).set_index('tradeDate')


if __name__ == '__main__':
    print get_dates_pattern(input_data=load_test_data()[4:70])