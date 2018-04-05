# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:27 2018

@author: Paulinka
"""
import Szkoły

# Docelowy program. Wiek jest ustalany z tym ile lat skończył w 2017. Ponieważ takie są dane. (jest też głupko odpornoć)
a=input('Podaj dzielnicę: ')
while a not in Szkoły.wybor:
    a=input('Podaj poprawną dzielnicę: ')
    
b= input('Podaj rok urodzenia: ')
rok=0
while rok == 0 :
    while type(b) != int :  
        try :   
            b=int(b)
        except ValueError:
            print('Podałe złą datę urodzenia! Podpowiedź (podaj cyferki)')
            b=input('Podaj poprawną :')
    if b > 2018:
        print('Pomyliłe się z datą bo takiej jeszcze nie było')
        b=input('Podaj poprawną datę: ')
    elif b < 1910:
        print('Raczej nie masz więcej niż 108 lat')
        b=input('Podaj poprawną datę: ')
    else:
        rok=b
        pass

f=input('Czy szukasz szkoły specjalnej (T/N): ')
while f not in [ 't','n','T','N' ]:
    print('Podałe złą odpowiedz! Podaj T lub N')
    f=input('Czy szukasz szkoły specjalnej (T/N): ')


c=int(2018-float(b))
d=a.upper()

# Pokazuje ile w danej dzielnicy jest dzieci w podanym wieku
print('\n W wieku', c , 'w dzielnicy', d , 'jest ', Szkoły.demografia.at[c,d],'dzieci \n')



            
if f == ('N') :
    if c < 4 :
        print('Pani/Pana dziecko jest za młode na szkołe.')
    elif c < 6 :
        podana=[Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==a]['Szkoła'],Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a]['Szkoła']]
        pobliska=[]
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                pobliska.append(Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==i]['Szkoła'])
                pobliska.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i]['Szkoła'])
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', podana,'\n Lub do szkoły w pobliżu :',pobliska)
    elif c < 16 :
        podana=[Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==a]['Szkoła'],Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a]['Szkoła']]
        pobliska=[]
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                pobliska.append(Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==i]['Szkoła'])
                pobliska.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i]['Szkoła'])
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', podana,'\n Lub do szkoły w pobliżu :',pobliska)
    elif c < 20 :
        podana=[Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==a]['Szkoła'],Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==a]['Szkoła']]
        pobliska=[]
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                pobliska.append(Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==i]['Szkoła'])
                pobliska.append(Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==i]['Szkoła'])
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', podana,'\n Lub do szkoły w pobliżu :',pobliska)
    else :
        podana=Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==a]['Szkoła']
        pobliska=[]
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                pobliska.append(Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==i]['Szkoła'])
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', podana,'\n Lub do szkoły w pobliżu :',pobliska)
else : 
     podana=Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==a]['Szkoła']
     pobliska=[]
     for i in Szkoły.Dzielnice.loc[a,:] :
         if i == None:
             pass #Aby omineło wartoci None
         else:
            pobliska.append(Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==i]['Szkoła'])
            print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:', podana,'\n Lub do szkoły w pobliżu :',pobliska)



