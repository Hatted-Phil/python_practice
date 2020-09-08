#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:48:13 2020

@author: finn
"""

s = input('Please enter a word:')
beta = ''
alpha = ''
for i in range(len(s)):
        if beta == '':
            beta = s[i]
        elif (s[i] >= (beta[-1])):
                beta += s[i]
        else:
                beta = s[i]
        if len(beta) > len(alpha):
            alpha = beta
print('Longest substring in alphabetical order is:' + alpha)
