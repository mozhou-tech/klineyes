#!/usr/bin/python
# -*- coding: UTF-8 -*-
from klineyes.classifier.patterns.candlestick.base import classifier_base


def basic_judge(x):
    '''
    对输入数据进行基础分类
    :param x:
    :return:
    '''
    return True


def data_preprocessing(x):
    return x


double = {
      'basic_judge': {
        'expression': basic_judge,
    },

    'data_preprocessing': {
        'callback': None
    },

    'flow': {
            'dark_cloud_cover': {
                'name_zh': '乌云盖顶',
                'feature': '乌云盖顶是由两支不同颜色及处于图表顶部的阴阳烛组成，属于一种见顶回落的转向形态，通常在一个上升趋势后出现。',
                'url': 'http://wiki.mbalib.com/wiki/%E4%B9%8C%E4%BA%91%E7%9B%96%E9%A1%B6',
                'expression': lambda x: True if x[0]['positive'] and not x[1]['positive'] and
                                                x[1]['open_price'] > x[0]['close_price'] and
                                                x[0]['pct_change'] >= 0.02 and x[1]['pct_change'] >= 0.02
                                                else False,
            }
    }
}


def classifier(candle_quant):
    '''
    根据蜡烛线特征数据，返回
    :param date:
    :param data:
    :return:
    '''
    if len(candle_quant)>= 2:
        return classifier_base(candle_quant, double, 'multi_double')
