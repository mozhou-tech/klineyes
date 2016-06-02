#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes import get_dates_pattern
from klineyes.common import load_test_data

print get_dates_pattern(load_test_data('000001'), ptypes=['hammer', 'line', 'star'])