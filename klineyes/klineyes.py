#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from common import data_validator, load_test_data
import classifier.single

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