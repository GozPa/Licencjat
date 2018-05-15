# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:22:47 2018

@author: Paulina
"""

import pandas as pd
from interpolacja import Interpolacja, Error
import numpy as np

# IloŚć ludzi w danych dzielnicach przewidywanie.
people = pd.read_excel('Demografia.xlsx', sheet_name = [14], skip_footer = 1, header = 1, usecols = 14)
people = pd.concat(people)

e=np.zeros(14)

people['PRZEWIDYWANE LICZBA LUDNOŚCI (liniowo)']=np.zeros(34)
people['PRZEWIDYWANE LICZBA LUDNOŚCI (kwadratowo)']=np.zeros(34)

people['Błąd - liniowo)']=np.zeros(34)
people['Błąd - kwadratowo)']=np.zeros(34)

a = range(2004,2018)
lista=list(range(0,34))
lista.pop(4)
lista.pop(15)
lista.pop(23)
lista.pop(25)

for i in lista:        
    s=people[i:i+1]
    for j in range(1,15):
        e[j-1]=s.iat[0,j] 
    people.iat[i,15]=Interpolacja(a,e,1)
    people.iat[i,16]=Interpolacja(a,e,2)
    people.iat[i,17]=Error(a,e,1)
    people.iat[i,18]=Error(a,e,2)
    
# Dla tych co mają b.d.
f = np.zeros(8)
b = range(2010,2018)

for i in (4,16,25,28):        
    s=people[i:i+1]
    for j in range(7,15):
        f[j-7]=s.iat[0,j] 
    people.iat[i,15]=Interpolacja(b,f,1)
    people.iat[i,16]=Interpolacja(b,f,2)
    people.iat[i,17]=Error(b,f,1)
    people.iat[i,18]=Error(b,f,2)
    
# Bezpieczeństwo z iloŚci przestepstw przewidywanie
    
security = pd.read_excel('Bezpieczeństwo.xlsx', sheet_name = [1], skiprows = [0,1], skip_footer = 124, usecols = [1,2,3,4], header = 1)
security = pd.concat(security)

y = np.zeros(3)

security['Przewidywana iloŚć przestępstw na 2018r. (liniowo)']=np.zeros(34)
security['Przewidywana iloŚć przestępstw na 2018r. (kwadratowo)']=np.zeros(34)

security['Błąd - liniowo)']=np.zeros(34)
security['Błąd - kwadratowo)']=np.zeros(34)

x = [2014,2015,2016]

for i in range(0,34):        
    b=security[i:i+1]
    for j in range(1,4):
        y[j-1]=b.iat[0,j] 
    security.iat[i,4]=Interpolacja(x,y,1)
    security.iat[i,5]=Interpolacja(x,y,2)
    security.iat[i,6]=Error(x,y,1)
    security.iat[i,7]=Error(x,y,2)
    
security['IloŚć przestepstw na 1000 mieszkańców']=np.zeros(34)
    
for k in range(0,34):
    security.iat[k,8]= ((security.iat[k,4] / people.iat[k,15])*1000)