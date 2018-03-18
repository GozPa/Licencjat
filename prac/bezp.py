# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:07:38 2018

@author: Paulina
"""

import pandas as pd
from interpolacja import Interpolacja, Error
import numpy as np
# Dane o bezpieczeństwie
Name = ['Dzielnica','PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2014 R.','PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2015 R.','PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2016 R.']
bezp = pd.read_excel('Bezpieczeństwo.xlsx',sheet_name = [1],skiprows = [0,1],skip_footer = 124, usecols = [1,8,9,10],header = 1,names = Name)

# Zamiana na Data Frame
bezp = pd.concat(bezp)
bezp = bezp.set_index('Dzielnica')

e=np.zeros(3)

bezp['PRZEWIDYWANE PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2018 R. (liniowo)']=np.zeros(34)
bezp['PRZEWIDYWANE PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2018 R. (kwadratowo)']=np.zeros(34)

bezp['Błąd - liniowo)']=np.zeros(34)
bezp['Błąd - kwadratowo)']=np.zeros(34)

a = [2014, 2015, 2016]


for i in range(0,34):        
    b=bezp[i:i+1]
    for j in range(0,3):
        e[j]=b.iat[0,j] 
    bezp.iat[i,3]=Interpolacja(a,e,1)
    bezp.iat[i,4]=Interpolacja(a,e,2)
    bezp.iat[i,5]=Error(a,e,1)
    bezp.iat[i,6]=Error(a,e,2)
