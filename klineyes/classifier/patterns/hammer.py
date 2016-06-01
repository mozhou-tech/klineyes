#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base import classifier_base
hammer = {
    'hammer': {
        "expression": lambda x: 'hammer_or_hanging' if x['top_height'] < 0.1 and x['bottom_height'] > x['entity_height'] * 2 and x['pct_amplitude'] >= 0.02 else False
    },
    'hanging': {
        "expression": lambda x: 'hammer_or_hanging' if x['top_height'] < 0.1 and x['bottom_height'] > x['entity_height'] * 2 and x['pct_amplitude'] >= 0.02 else False
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