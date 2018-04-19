# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:04:59 2018

@author: Paulina
"""

import pandas as pd


names=['Szkoła','Adres','Dzielnica','Telefon','Dyrektor']

# Złączenie szkół w jedno. 
szkoly = pd.read_excel("Szkoły.xlsx",sheet_name = [0,1,2,4,5],skiprows = [0,1,2,3], index_col = 0,header = 1,names = names)
szkoly3 = pd.read_excel("Szkoły.xlsx",sheet_name = 3,skiprows = [0,1,2,3],usecols = [0,1,2,3,4,5], index_col = 0,header = 1,names = names)
szkoly6 = pd.read_excel("Szkoły.xlsx",sheet_name = 6,skiprows = [0,1], index_col = 0,header = 1,names = names)
szkoly[3] = szkoly3
szkoly[6] = szkoly6
for i in range(0,7):
    szkoly[i] = szkoly[i].set_index('Szkoła')
szkolyDF = pd.concat([szkoly[0],szkoly[1],szkoly[2],szkoly[3],szkoly[4],szkoly[5],szkoly[6]],ignore_index=True)


# Wyodrebnienie danych o demograficznych.
demografia = pd.read_excel('Demografia.xlsx',sheet_name = [15], skip_footer = 6, usecols = range(0,103,3))
# Dopiero to zmienia mi na Data Frame
demografia = pd.concat(demografia)
# Zamienia nazwy żeby nie było ***-R.
demografia.rename(columns = lambda x: x[0:-2], inplace = True)
demografia = demografia.set_index('WIEK/lata ukończone\n(dane za 2017 r.)\nK - Kobiety\nM - Mężczyźni\nR - Raz')

# Storzenie dzielnic, z którymi granicą podane.
Dzielnice =pd.read_excel('dzielnice.xlsx', index_col = 0,)

wybor=['Aniołki','Brętowo','Brzeźno','Chełm','Jasień','Kokoszki','Krakowiec-Górki Zachodnie','Letnica','Matarnia','Młyniska','Nowy Port','Oliwa,Olszynka','Orunia-Św. Wojciech-Lipce','Osowa','Piecki - Migowo','Przeróbka','Przymorze Małe','Przymorze Wielkie','Rudniki','Siedlce','Stogi','Strzyża','Suchanino','Śródmieście','Ujeścisko-Łostowice','VII Dwór','Wrzeszcz Dolny','Wrzeszcz Górny','Wyspa Sobieszewska','Wzgórze Mickiewicza','Zaspa Młyniec','Zaspa Rozstaje','Żabianka-Wejhera-Jelit.Tysiąc.']