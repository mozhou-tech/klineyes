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
    if x[0]['turnover_val'] == 0.0:
        x[0]['turnover_val'] = 1
    if x[1]['turnover_val'] == 0.0:
        x[1]['turnover_val'] = 1
    if x[0]['lowest_price'] == 0.0:
        x[0]['lowest_price'] =1
    return x


double = {
      'basic_judge': {
        'expression': basic_judge,
    },

    'data_preprocessing': {
        'callback': data_preprocessing
    },

    'flow': {
        'dark_cloud_cover': {
            'name_zh': '乌云盖顶',
            'feature': '乌云盖顶是由两支不同颜色及处于图表顶部的阴阳烛组成，属于一种见顶回落的转向形态，通常在一个上升趋势后出现。',
            'url': 'http://wiki.mbalib.com/wiki/%E4%B9%8C%E4%BA%91%E7%9B%96%E9%A1%B6',
            'expression': lambda x: True if x[0]['positive'] and not x[1]['positive'] and
                                            x[1]['open_price'] > x[0]['close_price'] and
                                            x[0]['pct_change'] >= 0.02 and x[1]['pct_change'] >= 0.02 and
            # 第二支则为大阴烛，其开市价需比上日阳烛为高，而收市价则必须低于第一支烛烛身的一半为标准
                                            x[0]['close_price'] - ((x[0]['close_price'] - x[0]['open_price']) / 2) < x[1]['close_price'] and
                                            x[0]['open_price'] < x[1]['close_price']
                                            else False,
        },
        'dawn': {
            'name_zh': '曙光初现',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E6%9B%99%E5%85%89%E5%88%9D%E7%8E%B0',
            'expression': lambda x: True if not x[0]['positive'] and x[1]['positive'] and
                                                x[1]['open_price'] < x[0]['close_price'] and
                                                x[0]['pct_change'] >= 0.02 and x[1]['pct_change'] >= 0.015 and
                                                x[0]['open_price'] - ((x[0]['open_price'] - x[0]['close_price']) / 2) < x[1]['close_price'] and
                                                x[0]['open_price'] < x[1]['close_price']
                                                else False,
        },
        'positive_hold_negetive': {
            'name_zh': '阳抱阴',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E9%98%B3%E5%8C%85%E9%98%B4',
            'expression': lambda x: True if not x[0]['positive'] and x[1]['positive'] and
                                                x[1]['open_price'] < x[0]['close_price'] and
                                                x[1]['close_price'] > x[0]['open_price'] and
                                                0.006 < x[0]['pct_change'] < x[1]['pct_change']
                                                else False,
        },
        'negetive_hold_positive': {
            'name_zh': '阴抱阳',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E9%98%B4%E5%8C%85%E9%98%B3',
            'expression': lambda x: True if x[0]['positive'] and not x[1]['positive'] and
                                                x[1]['close_price'] < x[0]['open_price'] and
                                                x[1]['open_price'] > x[0]['close_price'] and
                                                0.006 <= x[0]['pct_change'] < x[1]['pct_change']
                                                else False,
        },
         'negetive_preg_positive': {
            'name_zh': '阴孕阳',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E9%98%B4%E5%AD%95%E9%98%B3',
            'expression': lambda x: True if not x[0]['positive'] and x[1]['positive'] and
                                                x[1]['close_price'] < x[0]['open_price'] and
                                                x[1]['open_price'] > x[0]['close_price'] and
                                                x[0]['pct_change'] > x[1]['pct_change'] >= 0.006
                                                else False,
        },
        'positive_preg_negetive': {
            'name_zh': '阴孕阳',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E9%98%B3%E5%AD%95%E9%98%B4',
            'expression': lambda x: True if x[0]['positive'] and not x[1]['positive'] and
                                                x[1]['open_price'] < x[0]['close_price'] and
                                                x[1]['close_price'] > x[0]['open_price'] and
                                                x[0]['pct_change'] > x[1]['pct_change'] >= 0.006
                                                else False,
        },
        'dip_needle': {
            'name_zh': '双针探底',
            'feature': '“双针探底”形态出现后，股价一般是立即反弹，走出一波气势不凡的上涨行情。',
            'url': "http://wiki.mbalib.com/wiki/%E5%8F%8C%E9%92%88%E6%8E%A2%E5%BA%95",
            'expression': lambda x: True if ((abs(x[0]['lowest_price'] / x[0]['lowest_price'] - x[1]['lowest_price'] / x[0]['lowest_price']))) < 0.001 and
                                                x[0]['bottom_height'] >= 0.5 and
                                                x[1]['bottom_height'] >= 0.5 and
                                                x[1]['pct_amplitude'] > 0.02 and
                                                x[0]['pct_amplitude'] > 0.02
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
