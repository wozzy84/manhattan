#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:16:59 2017

@author: radek
"""
import matplotlib.pyplot as plt

days_in_august = [1, 2, 3, 4, 5, 6, 7]
temps = [10, 12, 14, 23, 12, 24, 13]

plt.plot(days_in_august, temps)
plt.title("Temperatury w Sierpniu")
plt.xlabel("Dni kolejno od 13.08")
plt.ylabel("Temperatura")
plt.show()

