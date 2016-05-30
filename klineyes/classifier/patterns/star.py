#!/usr/bin/python
# -*- coding: UTF-8 -*-

star = {
    'normal': {
        'name_zh': '十字星',
        'feature': '',
        'expression': lambda x: True if x['top_height'] >= 0.4 and x['bottom_height'] >= 0.4 and x['entity_height'] <= 0.02 else False,
    },
    't': {
        'expression': lambda x: True if x['top_height'] < 0.05 and x['bottom_height'] > 0.3 and x['entity_height'] < 0.02 else False
    },
    'reverse_t': {
        'expression': lambda x: True if x['top_height'] > 0.3 and x['bottom_height'] < 0.03 and x['entity_height'] < 0.02 else False
    },
    'long': {
        'expression': lambda x: True if x['top_height'] >= 0.4 and x['bottom_height'] >= 0.4 and x['entity_height'] <= 0.08 and x['pct_amplitude'] >= 0.03 else False
    },
    'shooting': {
        'expression': lambda x: True if x['top_height'] > 0.5 and x['bottom_height'] >= 0.1 and x['entity_height'] >= 0.1 and x['pct_amplitude'] >= 0.03 else False
    },
    'yi': {
        'expression': lambda x: True if x['top_height'] == 0.0 and x['bottom_height'] == 0.0 and x['entity_height'] <= 0.01 else False
    }
}


def classifier(candle_quant):
    '''
    根据蜡烛线特征数据，返回
    :param date:
    :param data:
    :return:
    '''
    ret_rattern = None
    for pattern, dictX in star.items():
        if dictX['expression'](candle_quant) is True:
            ret_rattern = pattern
            break
    if ret_rattern is not None:
        return 'star.' + ret_rattern