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
    if len(input_data[0]) < 7:
        raise Exception('input array matrix at least 7 columns.')
    return input_data


def get_dates_by_pattern(input_data, pattern):
    '''

    :param input:
    :param pattern:
    :return:
    '''
    input_data = load_test_data()
    input_data = data_validator(input_data)
    df = pd.DataFrame(input_data, columns=['ticker', 'tradeDate', 'turnoverVol', 'closePrice', 'highestPrice', 'lowestPrice', 'openPrice'])
    for i, row in df.iterrows():
        if i > 0:
            row = row.append(pd.Series({'preClosePrice': df[i-1:i].closePrice.values[0]}))
            if classifier.single.get_candlestick_feature(row):
                print row.tradeDate


def get_day_pattern(input_data):
    pass



if __name__ == '__main__':
    print get_dates_by_pattern(input_data='input', pattern='star')