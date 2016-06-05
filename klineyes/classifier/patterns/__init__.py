#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.classifier.patterns.candlestick.hammer import classifier as classifier_hammer
from klineyes.classifier.patterns.candlestick.line import classifier as classifier_line
from klineyes.classifier.patterns.candlestick.star import classifier as classifier_star
from klineyes.classifier.patterns.candlestick.multi_double import classifier as classifier_multi_double
from klineyes.classifier.patterns.candlestick.multi_triple import classifier as classifier_multi_triple
from klineyes.classifier.patterns.candlestick.multi_fivefold import classifier as classifier_multi_fivefold

classifier_dict = {
    "star": classifier_star,
    "hammer": classifier_hammer,
    "line": classifier_line,
    "multi_double": classifier_multi_double,
    "multi_triple": classifier_multi_triple,
    "multi_fivefold": classifier_multi_fivefold
}
