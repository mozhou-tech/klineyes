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
    return np.array(df.values)


def data_validator(input_data):
    '''
    Data Validator
    :param input_data:
    :return:
    '''
    if isinstance(input_data, np.ndarray) is False:
        raise Exception('err data type.')
    if len(input_data) < 6:
        raise Exception('input array size is too small.')
    if len(input_data[0]) < 8:
        raise Exception('input array matrix at least 7 columns.')
    return input_data


def get_dates_by_pattern(input_data, pattern):
    '''
    获取图形对应的日期
    :param input:
    :param pattern:
    :return:
    '''
    input_data = load_test_data()
    input_data = data_validator(input_data)
    df = pd.DataFrame(input_data, columns=['ticker', 'tradeDate', 'turnoverVol', 'closePrice', 'highestPrice', 'lowestPrice', 'openPrice', 'preClosePrice'])
    for i, row in df.iterrows():
        feature = classifier.single.classifier_single_date(row)
        if feature is not None:
            print row.tradeDate +' '+ feature


def get_day_pattern(input_data):
    '''
    获取某一天的特征图形
    :param input_data:
    :return:
    '''
    pass



if __name__ == '__main__':
    (get_dates_by_pattern(input_data='input', pattern='star'))