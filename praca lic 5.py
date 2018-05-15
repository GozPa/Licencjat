# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:27 2018

@author: Paulinka
"""

import pandas as pd


names=['Szkoła','Adres','Dzielnica','Telefon','Dyrektor']

# Złączenie szkół w jedno. 
szkoly = pd.read_excel("Szkoły.xlsx",sheet_name = [0,1,2,4,5],skiprows = [0,1,2,3], index_col = 0,header = 1,names = names)
szkoly3 = pd.read_excel("Szkoły.xlsx",sheet_name = 3,skiprows = [0,1,2,3],usecols = [0,1,2,3,4,5], index_col = 0,header = 1,names = names)
szkoly6 = pd.read_excel("Szkoły.xlsx",sheet_name = 6,skiprows = [0,1], index_col = 0,header = 1,names = names)
szkoly[3] = szkoly3
szkoly[6] = szkoly6
szkolyDF = pd.concat([szkoly[0],szkoly[1],szkoly[2],szkoly[3],szkoly[4],szkoly[5],szkoly[6]],ignore_index=True)


# Wyodrebnienie danych o demograficznych.
demografia = pd.read_excel('Demografia.xlsx',sheet_name = [15], skip_footer = 6, usecols = range(0,103,3))
# Dopiero to zmienia mi na Data Frame
demografia = pd.concat(demografia)
# Zamienia nazwy żeby nie było ***-R.
demografia.rename(columns = lambda x: x[0:-2], inplace = True)
demografia = demografia.set_index('WIEK/lata ukończone\n(dane za 2017 r.)\nK - Kobiety\nM - Mężczyźni\nR - Raz')

# Dane o bezpieczeństwie
Name = ['Dzielnica','Wskaźnik przestępczosci rok 2015','Wskaźnik przestępczosci rok 2016','Zmiana % w latachy 2015/16']
bezp = pd.read_excel('Bezpieczeństwo.xlsx',sheet_name = [1],skiprows = [0,1],skip_footer = 125, usecols = [1,6,7,10],header = 1,names = Name)
# Zamiana na Data Frame
bezp = pd.concat(bezp)
bezp = bezp.set_index('Dzielnica')

# Tworzenie wektorów aby było wiadomo które dzielnice są koło siebie.
Aniołki = ['Aniołki','Wrzeszcz Górny','Wrzeszcz Dolny','Suchanino','Śródmieście','Młyniska','Siedlce']
Brętowo = ['Brętowo','VII Dwór','Wrzeszcz Górny','Piecki - Migowo','Jasień','Matarnia','Oliwa']
Brzeźno = ['Brzeźno','Wrzeszcz Dolny','Letnica','Nowy Port','Przymorze Wielkie','Zaspa Rozstaje']
Chełm = ['Chełm','Orunia-Św. Wojciech-Lipce','Siedlce','Śródmieście','Ujeścisko-Łostowice','Wzgórze Mickiewicza']
Jasień = ['Jasień','Brętowo','Matarnia','Piecki - Migowo','Ujeścisko-Łostowice']
Kokoszki = ['Kokoszki','Jasień','Matarnia']
Krakowiec = ['Krakowiec-Górki Zachodnie','Rudniki','Stogi','Wyspa Sobieszewska']
Letnica = ['Letnica','Wrzeszcz Dolny','Brzeźno','Młyniska','Nowy Port','Przeróbka']
Matarnia = ['Matarnia','Brętowo','Jasień','Kokoszki','Oliwa','Osowa']
Młyniska = ['Młyniska','Wrzeszcz Dolny','Aniołki','Letnica','Przeróbka','Śródmieście']
Port = ['Nowy Port','Brzeźno','Letnica','Przeróbka']
Oliwa = ['Oliwa','Brętowo','Matarnia','Osowa','Przymorze Małe','Strzyża','VII Dwór','Zaspa Młyniec','Żabianka-Wejhera-Jelit.Tysiąc.']
Olszynka = ['Olszynka','Orunia-Św. Wojciech-Lipce','Rudniki','Śródmieście']
Orunia = ['Orunia-Św. Wojciech-Lipce','Chełm','Olszynka','Śródmieście']
Osowa = ['Osowa','Matarnia','Oliwa']
Piecki= ['Piecki - Migowo','Brętowo','Jasień','Siedlce','Suchanino','Ujeścisko-Łostowice','Wrzeszcz Górny']
Przeróbka = ['Przeróbka','Letnica','Młyniska','Nowy Port','Rudniki','Stogi','Śródmieście']
PrzymorzeM = ['Przymorze Małe','Oliwa','Przymorze Wielkie','Zaspa Młyniec','Żabianka-Wejhera-Jelit.Tysiąc.']
PrzymorzeW = ['Przymorze Wielkie','Brzeźno','Przymorze Małe','Zaspa Rozstaje','Żabianka-Wejhera-Jelit.Tysiąc.']
Rudniki = ['Rudniki','Krakowiec-Górki Zachodnie','Olszynka','Przeróbka','Stogi','Śródmieście','Wyspa Sobieszewska']
Siedlce = ['Siedlce','Aniołki','Chełm','Piecki - Migowo','Suchanino','Śródmieście','Ujeścisko-Łostowice','Wzgórze Mickiewicza']
Stogi = ['Stogi','Krakowiec-Górki Zachodnie','Przeróbka','Rudniki']
Strzyża = ['Strzyża','Oliwa','VII Dwór','Wrzeszcz Górny','Zaspa Młyniec']
Suchanino = ['Suchanino','Aniołki','Piecki - Migowo','Siedlce','Wrzeszcz Górny']
Śródmieście = ['Śródmieście','Aniołki','Chełm','Młyniska','Olszynka','Orunia-Św. Wojciech-Lipce','Przeróbka','Rudniki','Siedlce']
Ujeścisko = ['Ujeścisko-Łostowice','Chełm','Jasień','Piecki - Migowo','Siedlce','Wzgórze Mickiewicza']
Dwór = ['VII Dwór','Brętowo','Oliwa','Strzyża','Wrzeszcz Górny']
WrzeszczD = ['Wrzeszcz Dolny','Aniołki','Brzeźno','Letnica','Młyniska','Zaspa Rozstaje','Wrzeszcz Górny','Zaspa Młyniec']
WrzeszczG = ['Wrzeszcz Górny','Wrzeszcz Dolny','Aniołki','Brętowo','Piecki - Migowo','Strzyża','Suchanino','Zaspa Młyniec','VII Dwór']
Wyspa = ['Wyspa Sobieszewska','Krakowiec-Górki Zachodnie','Rudniki']
Wzgórze = ['Wzgórze Mickiewicza','Chełm','Siedlce','Ujeścisko-Łostowice']
ZaspaM = ['Zaspa Młyniec','WrzeszczDolny','Oliwa','Przymorze Małe','Strzyża','Wrzeszcz Górny','Zaspa Rozstaje']
ZaspaR = ['Zaspa Rozstaje','Wrzeszcz Dolny','Brzeźno','Przymorze Wielkie','Zaspa Młyniec']
Żabianka = ['Żabianka-Wejhera-Jelit.Tysiąc.','Oliwa','Przymorze Małe','Przymorze Wielkie']

# Storzenie dzielnic, z którymi granicą podane.
Dzielnice = pd.DataFrame([Aniołki, Brętowo, Brzeźno, Chełm, Jasień, Kokoszki, Krakowiec, Letnica, Matarnia, Młyniska, Port, Oliwa, Olszynka, Orunia, Osowa, Piecki, Przeróbka, PrzymorzeM, PrzymorzeW, Rudniki, Siedlce, Stogi, Strzyża, Suchanino, Ujeścisko, WrzeszczG, WrzeszczD, Wyspa, Wzgórze, ZaspaM, ZaspaR, Żabianka, Śródmieście])
Dzielnice = Dzielnice.set_index(0)

# Docelowy program. Wiek jest ustalany z tym ile lat skończył w 2017. Ponieważ takie są dane.
a=input('Podaj dzielnicę: ')
b=input('Podaj rok urodzenia: ')
f=input('Czy szukasz szkoły specjalnej (T/N): ')
c=int(2018-float(b))
d=a.upper()

# Pokazuje ile w danej dzielnicy jest dzieci w podanym wieku
print('W wieku', c+1 , 'w dzielnicy', d , 'jest ', demografia.at[c,d],'dzieci \n')


# Wyszukuje szkoły dla danych dzielnic i wieku.
if f == ('N') :
    if c < 4 :
        print('Nie mam danych o żłobkach.\n')
    elif c < 6 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:\n',szkoly[0][szkoly[0]['Dzielnica']==a],'\n', szkoly[2][szkoly[2]['Dzielnica']==a],'\n')
    elif c < 16 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:\n',szkoly[1][szkoly[1]['Dzielnica']==a],'\n', szkoly[2][szkoly[2]['Dzielnica']==a],'\n')
    elif c < 20 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:\n',szkoly[3][szkoly[3]['Dzielnica']==a],'\n', szkoly[4][szkoly[4]['Dzielnica']==a],'\n')
    else :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:\n',szkoly[5][szkoly[5]['Dzielnica']==a],'\n')
else : 
     print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:\n',szkoly[6][szkoly[6]['Dzielnica']==a],'\n')
 
# Wyznaczenie pobliskich dzielnic.
# Dla okolicznych dzielnic.
for i in Dzielnice.loc[a,:] :
    if f == ('N') :
        if c < 4 :
            print('Nie mam danych o żłobkach.\n')
        elif c < 6 :
            print('Pani/Pana dziecko może iść do szkół w pobliskich dzielnicach:\n',szkoly[0][szkoly[0]['Dzielnica'] == i],'\n', szkoly[2][szkoly[2]['Dzielnica'] == i],'\n')
        elif c < 16 :
            print('Pani/Pana dziecko może isć do szkół w pobliskich dzielnicach:\n',szkoly[1][szkoly[1]['Dzielnica'] == i],'\n', szkoly[2][szkoly[2]['Dzielnica'] == i],'\n')
        elif c < 20 :
            print('Pani/Pana dziecko może isć do szkół w pobliskich dzielnicach:\n',szkoly[3][szkoly[3]['Dzielnica'] == i],'\n', szkoly[4][szkoly[4]['Dzielnica'] == i],'\n')
        else :
            print('Pani/Pana dziecko może isć do szkół w pobliskich dzielnicach:\n',szkoly[5][szkoly[5]['Dzielnica'] == i],'\n')
    else : 
        print('Pani/Pana dziecko może isć do szkół w pobliskich dzielnicach:\n',szkoly[6][szkoly[6]['Dzielnica'] == i],'\n')
            