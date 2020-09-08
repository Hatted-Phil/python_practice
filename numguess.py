#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:59:18 2020

@author: finn
"""

Low = 0
High = 100
answer = ''
print('Pick a number from 0 to 100!')
while True:
    guess = (High + Low) //2

    print('Is the number you chose ' + str(guess) + '?')
    print("Enter 'h' if the guess is too high.", end=' ') 
    print("Enter 'l' if the guess is too low.", end=' ')
    answer = input("Enter 'r' if I guessed right.")
    if answer == 'h':        
     High = guess
    elif answer == 'l':
     Low = guess
    elif answer == 'r':
     print("Game over. The number you thought of was:" + str(guess))
     break
    else:
     print('h, l or r, numbskull?')
    
