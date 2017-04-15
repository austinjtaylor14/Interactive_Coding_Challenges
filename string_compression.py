#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:03:49 2017

@author: Austin Taylor
"""

class CompressString(object):

    def compress(self, string):
        if string is None or not string:
            return(False)
        else:
            result = ''
            prev_char = string[0]
            count = 0
            for char in string:
                if char == prev_char:
                    count += 1
                else:
                    result += prev_char + str(count) if count > 1 else prev_char
                    prev_char = char
                    count = 1
            result += prev_char + str(count) if count > 1 else prev_char
            return(result if len(result) < len(string) else string)
        pass