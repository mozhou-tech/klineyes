#!/usr/bin/python
# -*- coding: UTF-8 -*-


def classifier_base(candle_quant, pattern_lib, ptype):
    '''
    根据蜡烛线特征数据，返回
    :param candle_quant: 蜡烛线的数据
    :param pattern_lib:  特征库
    :param ptype: 特征库类型
    :return:
    '''
    if pattern_lib['data_preprocessing']['callback'] is None:
        pass
    else:
        candle_quant = pattern_lib['data_preprocessing']['callback'](candle_quant)

    if pattern_lib['basic_judge']['expression'](candle_quant):
        ret_rattern = None
        for pattern, dictX in pattern_lib['flow'].items():
            if dictX['expression'](candle_quant) is True:
                ret_rattern = pattern
                break
        if ret_rattern is not None:
            return ptype + '.' + ret_rattern

