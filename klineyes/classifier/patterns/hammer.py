#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base import classifier_base


def basic_judge(x):
    '''
    对输入数据进行基础分类
    :param x:
    :return:
    '''
    return True


def data_preprocessing(x):
    return x

hammer = {
    'basic_judge': {
        'expression': basic_judge,
    },
    'data_preprocessing': {
        'callback': None
    },
    'flow': {
        'hammer': {
            'name_zh': '锤子线',
            'feature': '',
            'url': '',
            "expression": lambda x: True if x['top_height'] < 0.05 and
                                            x['bottom_height'] >= x['entity_height'] * 2 and
                                            x['pct_amplitude'] >= 0.025 and
                                            x['pct_change'] >= 0.006 else False
        },
        'hanging': {
            'name_zh': '上吊线',
            'feature': '',
            'url': '',
            "expression": lambda x: True if x['bottom_height'] < 0.05 and
                                            x['bottom_height'] >= x['entity_height'] * 2 and
                                            x['pct_amplitude'] >= 0.025 and
                                            x['pct_change'] >= 0.006 else False
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
    return classifier_base(candle_quant, hammer, 'hammer')
