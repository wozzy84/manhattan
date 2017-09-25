#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:44:29 2017

@author: radek
"""
import matplotlib.pyplot as plt
from io import BytesIO

class Plot(object):
    """Klasa jest odpowiedzialna za stworzneie i wyrenderowanie wykresu do pamięci"""
    
    def __init__(self, forecasts):
        self.forecasts = forecasts
    
    def make_plt(self):
        no_of_plots = len(self.forecasts)
        # Danzig, Warsaw, Breslau
        # self.forecasts => [{...}, {...}, {...}]
        fig, axs = plt.subplots(1, no_of_plots, sharey=True)
        # axs => [ax1, ax2, ax3]
        for uw, forecast in zip(axs, self.forecasts):
            uw.plot(forecast['xs']['values'], forecast['ys']['values'], label = forecast['ys']['label'])
            uw.set_title(forecast['title'])
            
        return (fig, plt)
    
    def plot(self):
        fig, plt = self.make_plt()
        
        imgdata = BytesIO()
        
        fig.set_size_inches(len(self.forecasts) * 5, 5)
        plt.savefig(imgdata, format='png')
        imgdata.seek(0)
        return imgdata
    