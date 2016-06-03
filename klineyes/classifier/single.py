#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division
from klineyes.classifier.patterns import classifier_single_dict
import pandas as pd
import numpy as np


def classifier_single_date(data, ptypes=['star', 'hammer', 'line']):
    '''
    获取某一天的形态
    :param ptypes: 要获取的蜡烛线特征类型
    :param data:
    :return:
    '''
    candle_quant = get_candlestick_feature(data)
    for ptype in ptypes:
        features = classifier_single_dict[ptype](candle_quant)
        if features is not None:
            return features


def get_candlestick_feature(data):
    '''
    单根蜡烛线 参数计算 top_height bottom_height entity_height pct_change pct_amplitude positive
    :param data:
    :return:
    '''
    negtive_filter = lambda x: None if x < 0 else x       # 过滤负值（无效数据）
    calc_rate = lambda relative_height, height : 0.0 if relative_height is None or height == 0.0 or height is None \
        or relative_height == 0.0 else relative_height / height     # 计算影线占实体的比例
    height = abs(data.highestPrice - data.lowestPrice)   # 蜡烛图长度,包括上下影线
    return {
        'jump_height': calc_rate(data.openPrice - data.preClosePrice, height),
        'top_height': calc_rate(negtive_filter(data.highestPrice - max(data.openPrice, data.closePrice)), height),
        'bottom_height': calc_rate(negtive_filter(min(data.openPrice, data.closePrice)-data.lowestPrice), height),
        'entity_height': calc_rate(abs(data.closePrice-data.openPrice), height),
        'pct_change': calc_rate(abs(data.closePrice-data.openPrice), data.preClosePrice),
        'pct_amplitude': calc_rate(abs(data.highestPrice-data.lowestPrice), data.preClosePrice),
        'positive': True if((data.closePrice - data.openPrice) > 0) else False,   # True=阳  False=阴
        'open_price': data.openPrice,
        'close_price': data.closePrice,
        'highest_price': data.highestPrice,
        'lowest_price': data.lowestPrice
    }
