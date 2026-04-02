#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:34:09 2026

@author: jathinmadineni
"""

import itertools

letters = "SENDMORY"
digits = range(10)

for perm in itertools.permutations(digits,len(letters)):
    mapping = dict(zip(letters,perm))

    if mapping['S']==0 or mapping['M']==0:
        continue

    send = 1000*mapping['S'] + 100*mapping['E'] + 10*mapping['N'] + mapping['D']
    more = 1000*mapping['M'] + 100*mapping['O'] + 10*mapping['R'] + mapping['E']
    money = 10000*mapping['M'] + 1000*mapping['O'] + 100*mapping['N'] + 10*mapping['E'] + mapping['Y']

    if send + more == money:
        print("Solution:\n",mapping)
        print(send,"+",more,"=",money)
        break