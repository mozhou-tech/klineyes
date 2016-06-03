#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.classifier.patterns.candlestick.hammer import classifier as classifier_hammer
from klineyes.classifier.patterns.candlestick.line import classifier as classifier_line
from klineyes.classifier.patterns.candlestick.star import classifier as classifier_star
from klineyes.classifier.patterns.candlestick.multi_double import classifier as classifier_multi_double

classifier_single_dict = {"star": classifier_star, "hammer": classifier_hammer, "line": classifier_line}
classifier_multi_dict = {"multi_double": classifier_multi_double}
