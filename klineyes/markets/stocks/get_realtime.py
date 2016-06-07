#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts


def get_realtime():
    return ts.get_today_all()
