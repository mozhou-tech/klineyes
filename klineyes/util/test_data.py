#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
from klineyes.util.common import BASE_DIR


def load_test_data(ticker='000001'):
    '''
    Load test test_data for develop
    :param ticker:
    :return: 	ticker	tradeDate	turnoverVol	closePrice	highestPrice	lowestPrice	openPrice
    '''
    return pd.read_csv(BASE_DIR+'/tests/test_data/'+ticker+'.csv', dtype={"ticker": np.str}, index_col=0)