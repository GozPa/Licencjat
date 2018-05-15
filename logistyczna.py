# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:40:46 2018

@author: Paulina
"""

from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

def Logistyczna(x,y):
    
lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(x, y)
plot_decision_regions(x, y, classifier=lr, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()