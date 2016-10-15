#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:04:49 2016

@author: ruth
"""

import backend

interventionConstraints = {}
interventionConstraints["Breastfeeding promotion"] = {}
interventionConstraints["Breastfeeding promotion"]['min'] = 6000000
interventionConstraints["Breastfeeding promotion"]['max'] = 10000000
interventionConstraints["Vitamin A supplementation"] = {}
interventionConstraints["Vitamin A supplementation"]['min'] = 4000000
interventionConstraints["Vitamin A supplementation"]['max'] = 5000000

best = backend.getResult(interventionConstraints)
print best