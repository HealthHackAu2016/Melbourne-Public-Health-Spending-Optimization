#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:04:49 2016

@author: ruth
"""

import backend

interventionConstraints = {}
interventionConstraints["Breastfeeding promotion"] = {}
interventionConstraints["Breastfeeding promotion"]['min'] = 1000
interventionConstraints["Breastfeeding promotion"]['max'] = 2000
interventionConstraints["Multiple micronutrient supplementation"] = {}
interventionConstraints["Multiple micronutrient supplementation"]['min'] = 1000
interventionConstraints["Multiple micronutrient supplementation"]['max'] = 2000

best = backend.getResult(interventionConstraints)
print best
