#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:31:34 2017

@author: Austin Taylor
"""

class Solution(object):

    def find_diff(s, t):
        for i in range(max(len(s), len(t))):
            try:
                if sorted(s)[i] != sorted(t)[i]:
                    return(sorted(t)[i])
            except:
                try:
                    return(s[i])
                except:
                    return(t[i])
        pass