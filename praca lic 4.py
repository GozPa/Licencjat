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
#szkolyDF = pd.concat([szkoly[0],szkoly[1],szkoly[2],szkoly[3],szkoly[4],szkoly[5],szkoly[6]],ignore_index=True)


# Wyodrebnienie danych o demograficznych 
demografia = pd.read_excel('Demografia.xlsx',sheet_name=[15], skip_footer = 6, usecols=range(0,103,3))
# Dopiero to zmienia mi na Data Frame
demografia=pd.concat(demografia)
# Zamienia nazwy żeby nie było ***-R
demografia.rename(columns=lambda x: x[0:-2], inplace=True)

demografia=demografia.set_index('WIEK/lata ukończone\n(dane za 2017 r.)\nK - Kobiety\nM - Mężczyźni\nR - Raz')
# Docelowy program. Wiek jest ustalany z tym ile lat skończył w 2017. Ponieważ takie są dane.
a=input('Podaj dzielnicę: ')
b=input('Podaj rok urodzenia: ')
f=input('Czy szukasz szkoły specjalnej (T/N): ')
c=int(2017-float(b))
d=a.upper()
# Pokazuje ile w danej dzielnicy jest dzieci w podanym wieku
print('W wieku', c , 'w dzielnicy', d , 'jest ', demografia.at[c,d],'dzieci \n')
# Wyszukuje szkoły dla danych dzielnic i wieku.
if f == ('N') :
    if c < 4 :
        print('Nie mam danych o żłobkach.\n')
    elif c < 6 :
        print('Pani/Pana dziecko może isć do tych szkół:\n',szkoly[0][szkoly[0]['Dzielnica']==a],'\n', szkoly[2][szkoly[2]['Dzielnica']==a],'\n')
    elif c < 16 :
        print('Pani/Pana dziecko może isć do tych szkół:\n',szkoly[1][szkoly[1]['Dzielnica']==a],'\n', szkoly[2][szkoly[2]['Dzielnica']==a],'\n')
    elif c < 20 :
        print('Pani/Pana dziecko może isć do tych szkół:\n',szkoly[3][szkoly[3]['Dzielnica']==a],'\n', szkoly[4][szkoly[4]['Dzielnica']==a],'\n')
    else :
        print('Pani/Pana dziecko może isć do tych szkół:\n',szkoly[5][szkoly[5]['Dzielnica']==a],'\n')
else : 
     print('Pani/Pana dziecko może isć do tych szkół:\n',szkoly[6][szkoly[6]['Dzielnica']==a],'\n')
    


