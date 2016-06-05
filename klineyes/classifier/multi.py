#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.classifier.patterns import classifier_multi_dict
from klineyes.classifier.single import get_candlestick_feature

def classifier_multi_date(data, ptypes=['multi_triple']):
    '''
    获取某一天的形态
    :param ptypes: 要获取的蜡烛线特征类型
    :param data:
    :return:
    '''
    candle_quant = get_multi_feature(data)
    for ptype in ptypes:
        features = classifier_multi_dict[ptype](candle_quant)
        if features is not None:
            return features


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