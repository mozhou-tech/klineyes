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


triple = {
      'basic_judge': {
        'expression': basic_judge,
    },

    'data_preprocessing': {
        'callback': data_preprocessing
    },

    'flow': {
        'morning_star': {
            'name_zh': '启明星',
            'feature': '一种行情见底转势的形态。这种形态如果出现在下降趋势中应引起注意，因为此时趋势已发出比较明确的反转信号，是一个非常好的买入时机。',
            'url': 'http://wiki.mbalib.com/wiki/%E5%90%AF%E6%98%8E%E6%98%9F',
            'expression': lambda x: True if x[0]['pct_change'] >= 0.02 and x[0]['positive'] is not True and
                                            x[1]['pct_change'] >= 0.01 and
                                            x[0]['close_price'] >= max(x[1]['open_price'], x[1]['close_price']) and
                                            x[2]['positive'] is True and
                                            x[2]['close_price'] >= x[0]['close_price'] + (x[0]['open_price']-x[0]['close_price']) * 0.5
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
    if len(candle_quant) == 3 and all(candle_quant):
        return classifier_base(candle_quant, triple, 'multi_triple')
