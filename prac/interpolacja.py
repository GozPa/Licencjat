# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:02:21 2018

@author: Paulina
"""
import numpy as np
#import matplotlib.pyplot as plt

def Interpolacja(x,y,s):
   #plt.scatter(x, y)  # Rysowanie ( tworzenie obszaru 1 )
   #xp = np.linspace(2014, 2018, 100)  # Rysowanie ( tworzenie obszaru 2 )
    z = np.polyfit(x, y, s)
    p = np.poly1d(z)   # Rysowanie 
   #plt.plot(x,y,".",xp,p(xp))  # Rysowanie ( wyświetlenie )
   #plt.show()
    return p(2018)

def Error(x,y,s):
    z = np.polyfit(x, y, s)
    p = np.poly1d(z)
    Error = np.zeros(3)
    for i in range(0,3):
        Error[i]=(p(x[i])-y[i])*(p(x[i])-y[i])
    Error = np.sqrt(np.sum(Error)/len(Error))
    return Error