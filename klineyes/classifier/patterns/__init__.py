#!/usr/bin/python
# -*- coding: UTF-8 -*-

from star import classifier as classifier_star
from line import classifier as classifier_line
from hammer import classifier as classifier_hammer

classifier_dict = {"star": classifier_star, "hammer": classifier_hammer, "line": classifier_line}
