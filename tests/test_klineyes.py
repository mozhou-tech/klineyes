from unittest import TestCase

import klineyes
from klineyes.util.test_data import load_test_data


class TestEyes(TestCase):

    def test_get_dates_pattern(self):
        '''
        testing
        :return:
        '''
        klineyes.get_dates_pattern(input_data=load_test_data(), ptypes=['hammer', 'line', 'star'])