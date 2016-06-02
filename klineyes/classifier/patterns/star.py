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
    pass


star = {
    'basic_judge': {
        'expression': basic_judge,
    },
    'data_preprocessing': {
        'callback': None
    },
    'flow': {
        'normal': {
            'name_zh': '十字星',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x['top_height'] >= 0.4 and
                                            x['bottom_height'] >= 0.4 and
                                            x['entity_height'] <= 0.02 else False,
        },
        't': {
            'name_zh': 'T字星',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x['top_height'] == 0.0 and
                                            x['bottom_height'] > 0.3 and
                                            x['entity_height'] < 0.02 and
                                            x['pct_amplitude'] >= 0.01 else False
        },
        'reverse_t': {
            'name_zh': '坟墓T字星',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x['top_height'] > 0.3 and
                                            x['bottom_height'] == 0.0 and
                                            x['entity_height'] < 0.02 and
                                            x['pct_amplitude'] >= 0.01 else False
        },
        'long': {
            'name_zh': '长十字星',
            'feature': '趋势的循环高点出现，见顶信号。趋势的循环低点出现，见底信号。上升趋势之末端出现，见顶信号。下跌趋势之末端出现，见底信号。',
            'url': 'http://wiki.mbalib.com/wiki/%E9%95%BF%E5%8D%81%E5%AD%97%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] >= 0.4 and
                                            x['bottom_height'] >= 0.4 and
                                            x['entity_height'] <= 0.08 and
                                            x['pct_amplitude'] >= 0.03 else False
        },
        'shooting': {
            'name_zh': '射击之星',
            'feature': '射击之星形态如果在高位出现，行情下跌的可能性较大。',
            'url': 'http://wiki.mbalib.com/wiki/%E6%B5%81%E6%98%9F%E7%BA%BF',
            'expression': lambda x: True if x['bottom_height'] >= 0.1 and
                                            x['entity_height'] <= 0.18 and
                                            x['top_height'] >= x['entity_height'] * 2 and
                                            abs(x['jump_height']) > 0.1 and
                                            x['pct_amplitude'] >= 0.03 else False
        },
        'yi': {
            'name_zh': '',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x['top_height'] == 0.0 and
                                             x['bottom_height'] == 0.0 and
                                             x['entity_height'] <= 0.01 else False
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
    return classifier_base(candle_quant, star, 'star')
