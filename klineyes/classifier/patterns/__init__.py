#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.classifier.patterns.star import classifier as classifier_star
from klineyes.classifier.patterns.line import classifier as classifier_line
from klineyes.classifier.patterns.hammer import classifier as classifier_hammer

classifier_dict = {"star": classifier_star, "hammer": classifier_hammer, "line": classifier_line}
