#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.classifier.patterns import classifier_dict
from klineyes.classifier.single import get_candlestick_feature

def classifier_multi_date(data, ptype):
    '''
    获取某一天的形态
    :param ptypes: 要获取的蜡烛线特征类型
    :param data:
    :return:
    '''
    if data is not None:
        candle_quant = get_multi_feature(data)

        features = classifier_dict[ptype](candle_quant)
        if features is not None:
            return features
    else:
        Exception('classifier_multi_date func get None data')


def get_multi_feature(df):
    '''
    从single模块中获取蜡烛图特征数据
    :param df:
    :return:
    '''
    features = []

    for i, row in df.iterrows():
        features.append(get_candlestick_feature(row))
    return features