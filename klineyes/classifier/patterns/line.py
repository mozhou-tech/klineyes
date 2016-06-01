#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base import classifier_base
line = {
    'basic_judge': {
        'expression': True,
    },
    'flow': {
        'positive': {
            'name_zh': '十字星',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x['top_height'] >= 0.4 and x['bottom_height'] >= 0.4 and x['entity_height'] <= 0.02 else False,
        },
    }

}


def classifier(candle_quant):
    '''
    根据蜡烛线特征数据，返回
    :param date:
    :param data:
    :return:
    '''
    return classifier_base(candle_quant, line, 'line')