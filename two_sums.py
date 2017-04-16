#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:26:19 2017

@author: Austin Taylor
"""

class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError()
        elif not nums or not val:
            raise ValueError()
        else:
            for index, list_item in enumerate(nums):
                diff = val - list_item
                if diff in nums:
                    return([index, nums.index(diff)])
        pass
