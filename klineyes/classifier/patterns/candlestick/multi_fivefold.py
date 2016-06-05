#!/usr/bin/python
# -*- coding: UTF-8 -*-
from klineyes.classifier.patterns.candlestick.base import classifier_base
from klineyes.classifier.patterns.candlestick.star import star


def basic_judge(x):
    '''
    对输入数据进行基础分类
    :param x:
    :return:
    '''
    return True


def data_preprocessing(x):

    return x


def normal_star_chain(x):
    '''
    判断是否是连续十字星
    :param x:
    :return:
    '''
    star_count = 0
    for i in x:
        if star['flow']['normal']['expression'](i):
            star_count = star_count + 1

    return True if star_count >= 3 else False


def dip_needle(x):
    '''
    隔几个蜡烛线探底的
    :param x:
    :return:
    '''
    min_price_round = round(min(x[0]['lowest_price'], x[1]['lowest_price'], x[2]['lowest_price'], x[3]['lowest_price'], x[4]['lowest_price']), 2)
    dip_count = 0
    for i in x:
        if min_price_round == i['lowest_price'] and i['bottom_height'] > 0.5 and i['pct_amplitude'] >= 0.05:
            dip_count = dip_count + 1
    return True if dip_count >= 2 else False




fivefold = {
      'basic_judge': {
        'expression': basic_judge,
    },

    'data_preprocessing': {
        'callback': data_preprocessing
    },

    'flow': {
        'rising_three_method': {
            'name_zh': '上升三法',
            'feature': '多方在蓄积力量，饲机上攻。',
            'url': '',
            'expression': lambda x: True if x[0]['positive'] is True and x[4]['positive'] is True and
                                             x[0]['open_price'] < x[1]['open_price'] < x[0]['close_price'] and
                                             x[0]['open_price'] < x[1]['close_price'] < x[0]['close_price'] and
                                             x[0]['open_price'] < x[2]['open_price'] < x[0]['close_price'] and
                                             x[0]['open_price'] < x[2]['close_price'] < x[0]['close_price'] and
                                             x[0]['open_price'] < x[3]['open_price'] < x[0]['close_price'] and
                                             x[0]['open_price'] < x[3]['close_price'] < x[0]['close_price'] and
                                             x[0]['pct_change'] >= 0.04 and x[4]['pct_change'] >= 0.03
                                             else False,
        },
         'falling_three_method': {
            'name_zh': '下降三法',
            'feature': '',
            'url': '',
            'expression': lambda x: True if x[0]['positive'] is False and x[4]['positive'] is False and
                                             x[0]['open_price'] > x[1]['open_price'] > x[0]['close_price'] and
                                             x[0]['open_price'] > x[1]['close_price'] > x[0]['close_price'] and
                                             x[0]['open_price'] > x[2]['open_price'] > x[0]['close_price'] and
                                             x[0]['open_price'] > x[2]['close_price'] > x[0]['close_price'] and
                                             x[0]['open_price'] > x[3]['open_price'] > x[0]['close_price'] and
                                             x[0]['open_price'] > x[3]['close_price'] > x[0]['close_price'] and
                                             x[4]['pct_change'] >= 0.02
                                             else False,
        },
        'dip_needle': {
            'name_zh': '双针探底',
            'feature': '双针探底',
            'url': 'http://wiki.mbalib.com/wiki/%E4%B9%8C%E4%BA%91%E7%9B%96%E9%A1%B6',
            'expression': dip_needle,
        },
         'normal_star_chain': {
            'name_zh': '连续十字星',
            'feature': '中继形态',
            'url': 'http://wiki.mbalib.com/wiki/%E8%BF%9E%E7%BB%AD%E5%8D%81%E5%AD%97%E6%98%9F',
            'expression': normal_star_chain,
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
    if len(candle_quant) == 5 and all(candle_quant):
        return classifier_base(candle_quant, fivefold, 'multi_fivefold')
