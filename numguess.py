#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:59:18 2020

@author: finn
"""

Low = 0
High = 100
answer = ''
print('Please think of a number between 0 and 100!')
while True:
    guess = (High + Low) //2

    print('Is your secret number ' + str(guess))
    print("Enter 'h' to indicate the guess is too high.", end=' ') 
    print("Enter 'l' to indicate the guess is too low.", end=' ')
    answer = input("Enter 'c' to indicate I guessed correctly.")
    if answer == 'h':        
     High = guess
    elif answer == 'l':
     Low = guess
    elif answer == 'c':
     print("Game over. Your secret number was:" + str(guess))
     break
    else:
     print('h, l or c, dingbat?')
    