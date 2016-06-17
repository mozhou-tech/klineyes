#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import talib as ta


def line_intersections(df, columns):
    '''
    columns fast in 0 计算两条直线的交点
    :param df:
    :param columns:
    :return:
    '''
    min_macddif = df.macddif.min()
    intersections = []
    point = {}
    for i, row in df.iterrows():
        point['00'] = df[i-1:i][columns[0]].values   # line1  第一个点
        point['10'] = df[i-1:i][columns[1]].values   # line2  第一个点
        point['01'] = df[i:i+1][columns[0]].values   # line1  第二个点
        point['11'] = df[i:i+1][columns[1]].values   # line2  第二个点
        if (point['00'] >= point['10']) and (point['01'] <= point['11']):
            intersections.append({"macd_shape": 'death'})
        elif (point['00'] <= point['10']) and (point['01'] >= point['11']):
            intersections.append({"macd_shape": 'golden'})
        elif (point['00'] <= np.float64(0)) and (point['01'] >= np.float64(0)):  # 自下而上经过zero轴，以快线为准
            intersections.append({"macd_shape": 'inc_touch_zero'})
        elif (point['00'] >= np.float64(0)) and (point['01'] <= np.float64(0)):  # 自上而下经过zero轴，以快线为准
            intersections.append({"macd_shape": 'dec_touch_zero'})
        elif (row.macddif == min_macddif):
            intersections.append({"macd_shape": 'min_point'})
        else:
            intersections.append({"macd_shape": None})
    return pd.DataFrame(intersections).reset_index(drop=True)


def price_divergence(df):
    '''
    MACD close 背离判断
    should have column date,
    :param df:
    :return:
    '''
    print df.price_change.sum()


