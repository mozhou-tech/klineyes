#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

def line_intersections(df, columns):
    '''
    columns fast in 0 计算两条直线的交点
    :param df:
    :param columns:
    :return:
    '''

    intersections = []
    point = {}
    for i, row in df.iterrows():
        point['00'] = df[i-1:i][columns[0]].values
        point['10'] = df[i-1:i][columns[1]].values
        point['01'] = df[i:i+1][columns[0]].values
        point['11'] = df[i:i+1][columns[1]].values
        if (point['00'] >= point['10']) and (point['01'] <= point['11']) and (point['00'] >= np.float64(0)):
            intersections.append({"macd_shape": 'death'})
        elif (point['00'] <= point['10']) and (point['01'] >= point['11']) and (point['00'] <= np.float64(0)):
            intersections.append({"macd_shape": 'golden'})
        else:
            intersections.append({"macd_shape": None})
    return pd.DataFrame(intersections).reset_index().drop('index', 1)


