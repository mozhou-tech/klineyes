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


sevenfold = {
      'basic_judge': {
        'expression': basic_judge,
    },

    'data_preprocessing': {
        'callback': data_preprocessing
    },

    'flow': {
        'dip_needle': {
            'name_zh': '双针探底',
            'feature': '双针探底',
            'url': 'http://wiki.mbalib.com/wiki/%E4%B9%8C%E4%BA%91%E7%9B%96%E9%A1%B6',
            'expression': None,
        },
         'normal_star_chain': {
            'name_zh': '连续十字星',
            'feature': '双针探底',
            'url': 'http://wiki.mbalib.com/wiki/%E8%BF%9E%E7%BB%AD%E5%8D%81%E5%AD%97%E6%98%9F',
            'expression': None,
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
        return classifier_base(candle_quant, sevenfold, 'multi_sevenfold')
