#!/usr/bin/python
# -*- coding: UTF-8 -*-

hammer = {
    'hammer': {
        "expression": lambda x: 'hammer_or_hanging' if x['top_height'] < 0.1 and x['bottom_height'] > x['entity_height'] * 2 and x['pct_amplitude'] >= 0.02 else False
    },
    'hanging': {
        "expression": lambda x: 'hammer_or_hanging' if x['top_height'] < 0.1 and x['bottom_height'] > x['entity_height'] * 2 and x['pct_amplitude'] >= 0.02 else False
    }
}