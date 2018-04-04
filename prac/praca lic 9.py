# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:27 2018

@author: Paulinka
"""
import Szkoły
from toint import Toint 

# Docelowy program. Wiek jest ustalany z tym ile lat skończył w 2017. Ponieważ takie są dane.
a=input('Podaj dzielnicę: ')
b= input('Podaj rok urodzenia: ')
while Toint(b) is not range(1910,2018,1):        
    if b > 2018:
        print('Pomyliłe się z datą bo takiej jeszcze nie było')
        b=input('Podaj poprawną :')
        Toint(b)
    elif b < 1910:
        print('Raczej nie masz więcej niż 108 lat')
        b=input('Podaj poprawną :')
        Toint(b)
    else:
        pass

f=input('Czy szukasz szkoły specjalnej (T/N): ')
while f is [ 't',' n','T','N' ]:
    print('Podałe złą odpowiedz! Podaj T lub N')
    f=input('Czy szukasz szkoły specjalnej (T/N): ')

c=int(2018-float(b))
d=a.upper()

# Pokazuje ile w danej dzielnicy jest dzieci w podanym wieku
print('W wieku', c , 'w dzielnicy', d , 'jest ', Szkoły.demografia.at[c,d],'dzieci \n')

k=[0,0,0,0,0,0]
# Działanie na celu zlikwidowania powiadomienia DataFrame  is empty
for i in range(0, 6):
    if Szkoły.szkoly[i][Szkoły.szkoly[i]['Dzielnica']==a].empty == True:
       pass
    else:
        k[i]=Szkoły.szkoly[i][Szkoły.szkoly[i]['Dzielnica']==a]


# Wyszukuje szkoły dla danych dzielnic i wieku.
if f == ('N') :
    if c < 4 :
        print('Nie mam danych o żłobkach.')
    elif c < 6 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', k[0],'\n', k[2],'\n')
    elif c < 16 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', k[1],'\n', k[2],'\n')
    elif c < 20 :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', k[3],'\n', k[4],'\n')
    else :
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', k[5],'\n')
else : 
     print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:',k[6] ,'\n')
 

t=[0,0,0,0,0,0]     
# Wyznaczenie pobliskich dzielnic.
print('Pani/Pana dziecko może iść do tych szkół w pobliskich dzielnicach:\n')
for i in Szkoły.Dzielnice.loc[a,:] :
    if i == None:
       pass #Aby omineło wartoci None
    else:
         # Działanie na celu zlikwidowania powiadomienia DataFrame  is empty`
        for n in range(0,6):
            if Szkoły.szkoly[n][Szkoły.szkoly[n]['Dzielnica']==i].empty == True:
                pass
            else:
                t[n]=Szkoły.szkoly[n][Szkoły.szkoly[n]['Dzielnica']==i]
        # Dla okolicznych dzielnic.
        if f == ('N') :
            if c < 4 :
                print('Nie mam danych o żłobkach.\n')
            elif c < 6 :
                print( t[0], t[2],'\n')
            elif c < 16 :
                print( t[1], t[2],'\n')
            elif c < 20 :
                print( t[3], t[4],'\n')
            else :
                print( t[5],'\n')
        else : 
            print( t[6],'\n')
                
#dane ze szkoły wyniki, i iloć dziecie w szkołach, bezpieczeństwo