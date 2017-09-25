#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:44:12 2017

@author: radek
"""

import matplotlib.pyplot as plt
import numpy as np

dni_tygodnia = np.arange(1, 8)
temperatury_w_lipcu = [10, 8, 13, 14, 15, 16, 19]
temperatury_w_sierpniu = [11, 2, 3, 12, 14, 15, 21]

temperatury = [
        { 'title': 'Lipiec',
          'values': temperatury_w_lipcu }, 
        { 'title': 'Sierpień',
          'values': temperatury_w_sierpniu }
        ]

_fig, axs = plt.subplots(1, 2, figsize=(20, 10))

# axs = [pierwszy_uklad, drugi_uklad]
# enumerate(axs) => [(0, pierwszy_uklad), (1, drugi_uklad)]
for index, ax in enumerate(axs):
    ax.plot(dni_tygodnia, temperatury[index]['values'])
    ax.set_title(temperatury[index]['title'])

plt.show()
