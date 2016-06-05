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
                                            x[0]['close_price'] > max(x[1]['open_price'], x[1]['close_price']) and
                                            x[2]['positive'] is True and
                                            x[2]['close_price'] >= (x[0]['close_price'] + (x[0]['open_price']-x[0]['close_price']) * 0.5)
                                            else False,
        },
        'evening_star': {
            'name_zh': '黄昏星',
            'feature': '较强烈的上升趋势中出现反转的信号。',
            'url': 'http://wiki.mbalib.com/wiki/%E9%BB%84%E6%98%8F%E6%98%9F',
            'expression': lambda x: True if x[0]['positive'] is True and x[2]['positive'] is False and
                                            x[0]['pct_change'] >= 0.02 and
                                            x[0]['close_price'] < min(x[1]['open_price'], x[1]['close_price']) and
                                            x[2]['close_price'] <= (x[0]['open_price'] + (x[0]['close_price']-x[0]['open_price']) * 0.5)
                                            else False,
        },
        'three_crows': {
            'name_zh': '三只乌鸦',
            'feature': '三根向下的阴线持续下跌，后市看淡。',
            'url': 'http://wiki.mbalib.com/wiki/%E4%B8%89%E5%8F%AA%E4%B9%8C%E9%B8%A6',
            'expression': lambda x: True if x[0]['positive'] is False and x[1]['positive'] is False and x[2]['positive'] is False and
                                            x[0]['lowest_price'] > x[1]['close_price'] and
                                            x[1]['lowest_price'] > x[2]['close_price'] and
                                            x[0]['close_price'] <= x[1]['open_price'] <= x[0]['open_price'] and
                                            x[1]['close_price'] <= x[2]['open_price'] <= x[1]['open_price'] and
                                            x[0]['bottom_height'] < 0.3 and x[1]['bottom_height'] < 0.3 and
                                            x[2]['bottom_height'] < 0.1
                                            else False,
        },
        'red_soldier': {
            'name_zh': '红三兵',
            'feature': '出现在底部或横盘，突破压力位配合成交量放大酝酿一波行情，止损在下方支撑位。',
            'url': 'http://wiki.mbalib.com/wiki/%E7%BA%A2%E4%B8%89%E5%85%B5',
            'expression': lambda x: True if x[0]['positive'] is True and x[1]['positive'] is True and x[2]['positive'] is True and
                                           x[0]['pct_change'] > 0.003 and x[1]['pct_change'] > 0.003 and x[2]['pct_change'] > 0.003 and
                                           x[0]['top_height'] < 0.2 and x[1]['top_height'] < 0.25 and x[2]['top_height'] < 0.3
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
