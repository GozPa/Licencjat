# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:27 2018

@author: Paulinka
"""

import pandas as pd

names=['Szkoła','Adres','Dzielnica','Telefon','Dyrektor']
#Z łączenie szkół w jedno 
szkoly = pd.read_excel("Szkoły.xlsx",sheet_name=[0,1,2,4,5],skiprows=[0,1,2,3], index_col = 0,header = 1,names=names)
szkoly3 = pd.read_excel("Szkoły.xlsx",sheet_name=3,skiprows=[0,1,2,3],usecols=[0,1,2,3,4,5], index_col = 0,header = 1,names=names)
szkoly6 = pd.read_excel("Szkoły.xlsx",sheet_name=6,skiprows=[0,1], index_col = 0,header = 1,names=names)
szkoly[3] = szkoly3
szkoly[6] = szkoly6
szkoly[3] = szkoly3
szkoly[6] = szkoly6
szkolyDF = pd.concat([szkoly[0],szkoly[1],szkoly[2],szkoly[3],szkoly[4],szkoly[5],szkoly[6]],ignore_index=True)


# Wyodrebnienie danych o demograficznych 
demografia = pd.read_excel('Demografia.xlsx',sheet_name=[15], skip_footer=6, usecols=range(0,103,3))
# Dopiero to zmienia mi na Data Frame
demografia=pd.concat(demografia)


# Docelowy program.
a=input('Podaj dzielnicę: ')
b=input('Podaj rok urodzenia: ')
c=2017-float(b)
print('Pani/Pana dziecko w wieku' , c , 'lat w dzielnicy' , a , 'może pojsć do tych szkół: ', szkolyDF[szkolyDF['Dzielnica']==a] )
# Nie dzieła ale narazie luz 
#print('W wieku', c , 'w dzielnicy', a , 'jest ', demografia.at[a,c],'dzieci')