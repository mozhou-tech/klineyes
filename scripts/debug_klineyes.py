#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes import get_dates_pattern2
from klineyes.util.test_data import load_test_data

print get_dates_pattern2(load_test_data('000001'), ptypes=['hammer', 'line', 'star'])
# print get_dates_pattern(load_test_data('000001'), ptypes=['hammer', 'line', 'star'])

