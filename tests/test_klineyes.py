from unittest import TestCase

import klineyes

from klineyes.common import load_test_data


class TestEyes(TestCase):

    def test_is_string(self):
        klineyes.get_dates_pattern(input_data=load_test_data(), ptypes=['hammer', 'line', 'star'])