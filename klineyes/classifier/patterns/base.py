#!/usr/bin/python
# -*- coding: UTF-8 -*-


def classifier_base(candle_quant, pattern_lib, type):
    '''
    根据蜡烛线特征数据，返回
    :param date:
    :param data:
    :return:
    '''
    ret_rattern = None
    for pattern, dictX in pattern_lib.items():
        if dictX['expression'](candle_quant) is True:
            ret_rattern = pattern
            break
    if ret_rattern is not None:
        return type + '.' + ret_rattern

