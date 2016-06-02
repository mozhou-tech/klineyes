#!/usr/bin/python
# -*- coding: UTF-8 -*-
from klineyes.classifier.patterns.base import classifier_base

def basic_judge(x):
    '''
    对输入数据进行基础分类
    :param x:
    :return:
    '''
    return True


def data_preprocessing(x):
    return x

line = {
    'basic_judge': {
        'expression': basic_judge,
    },
    'data_preprocessing': {
        'callback': None
    },
    'flow': {

        'bare_positive': {
            'name_zh': '光头光脚阳线',
            'feature': '这种K线是一种强烈的上涨信号，表明多方已经牢固控制盘面，逐浪上攻，步步逼空，涨势强烈。股价仍有进一步向上扩展空间的能力，如果K线实体越长，说明上涨动力越强。',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E5%A4%B4%E5%85%89%E8%84%9A%E9%98%B3%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] == 0.0 and
                                            x['bottom_height'] == 0.0 and
                                            x['pct_change'] >= 0.01 and
                                            x['positive'] else False,

        },
        'bare_negative': {
            'name_zh': '光头光脚阴线',
            'feature': '这种K线是一种强烈的卖出信号，表明股价仍有进一步下跌的可能，如果K线实体越长，说明做空动力越强。如果光头光脚阴线出现的同时还伴随着放量的特征，则是一种明显的见顶特征。如果股价走出逐波下跌的行情，这说明空方已占尽优势，多方无力抵抗，股价被逐步打低，后市看淡。',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E5%A4%B4%E5%85%89%E8%84%9A%E9%98%B4%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] == 0.0 and
                                            x['bottom_height'] == 0.0 and
                                            x['pct_change'] >= 0.01 and
                                            not x['positive'] else False,

        },
        'barefeet_negative': {
            'name_zh': '光脚阴线',
            'feature': '卖方力量强大，抛压沉重，买方有抵抗但微弱无力。',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E8%84%9A%E9%98%B4%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] >= 0.15 and
                                            x['bottom_height'] == 0.0 and
                                            x['pct_change'] >= 0.02 and
                                            not x['positive'] else False,

        },
        'barefeet_positive': {
            'name_zh': '光脚阳线',
            'feature': '经常出现在上涨途中、上涨末期或股价向上运行时遇到密集成交区，表明多方上攻受阻，上影线越长，表明上档压力越大，阳线实体越长，表明多方力量越强。但在高价位处多空双方有分歧',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E8%84%9A%E9%98%B3%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] >= 0.15 and
                                            x['bottom_height'] == 0.0 and
                                            x['pct_change'] >= 0.02 and
                                            x['positive'] else False,
        },
        'barehead_negative': {
            'name_zh': '光头阴线',
            'feature': '一开盘卖方力量就特别大，股价一直处于下跌状态，但当跌到低位时，受到买盘力量的推升，股价得到支撑，由此股价可能会形成反弹。',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E5%A4%B4%E9%98%B4%E7%BA%BF',
            'expression': lambda x: True if x['bottom_height'] >= 0.15 and
                                            x['top_height'] == 0.0 and
                                            x['pct_change'] >= 0.02 and
                                            not x['positive'] else False,
        },
        'barehead_positive': {
            'name_zh': '光头阳线',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E5%85%89%E5%A4%B4%E9%98%B3%E7%BA%BF',
            'expression': lambda x: True if x['bottom_height'] >= 0.15 and
                                            x['top_height'] == 0.0 and
                                            x['pct_change'] >= 0.02 and
                                            x['positive'] else False,
        },
        'long_positive': {
            'name_zh': '大阳线',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E5%A4%A7%E9%98%B3%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] <= 0.1 and
                                            x['bottom_height'] <= 0.1 and
                                            x['pct_change'] >= 0.08 and
                                            x['positive'] else False,
        },
        'long_negative': {
            'name_zh': '大阴线',
            'feature': '',
            'url': 'http://wiki.mbalib.com/wiki/%E5%A4%A7%E9%98%B4%E7%BA%BF',
            'expression': lambda x: True if x['top_height'] <= 0.1 and
                                            x['bottom_height'] <= 0.1 and
                                            x['pct_change'] >= 0.08 and
                                            not x['positive'] else False,
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
    return classifier_base(candle_quant, line, 'line')