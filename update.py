#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys,os
try:
    if sys.argv[1]=='push':
        os.system("cp data/* /usr/share/games/fortunes/i")
    elif sys.argv[1]=='pull':
        os.system("cp /usr/share/games/fortunes/* data")
    else:
        print("Usage: update [push] [pull]")
except:
    print("Usage: update [push] [pull]")
