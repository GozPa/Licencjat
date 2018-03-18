# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:02:21 2018

@author: Paulina
"""
import numpy as np

def Interpolacja(x,y,s):
    z = np.polyfit(x, y, s)
    p = np.poly1d(z)
    return p(2018)

def Error(x,y,s):
    z = np.polyfit(x, y, s)
    p = np.poly1d(z)
    Error = np.zeros(3)
    for i in range(0,3):
        Error[i]=(p(x[i])-y[i])*(p(x[i])-y[i])
    Error = np.sqrt(np.sum(Error))
    return Error