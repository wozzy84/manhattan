#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:02:44 2017

@author: radek
"""

import matplotlib.pyplot as plt
import numpy as np

X_LN = np.linspace(0.001, 9, 256)
X_EXP = np.linspace(-8, 3, 256)

Y_EXP = np.exp(X_EXP)
Y_LN = np.log(X_LN)

plt.figure(figsize=(12, 12), dpi=80)
plt.plot(X_LN, 
         Y_LN,
         color='red',
         linewidth=2.5,
         linestyle="-",
         label="ln(x)"
         )

plt.plot(X_EXP,
         Y_EXP,
         color='blue',
         linewidth=2.5,
         linestyle="-",
         label=r'$e^{x}$'
         )

ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xticks(np.arange(-8, 8, 1))
plt.yticks(np.arange(-7, 24, 1))
plt.legend(loc=2, prop={ 'size': 30 })
plt.show()