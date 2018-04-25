# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:27 2018

@author: Paulinka
"""
import Szkoły
import bezp
# Docelowy program. Wiek jest ustalany z tym ile lat skończył w 2017. Ponieważ takie są dane. (jest też głupko odpornoć)
a=input('Podaj dzielnicę: ')
while a not in Szkoły.wybor:
    print('Podałeś złą dzielnice. tu masz podpowiedź jakie są: \n',Szkoły.wybor)
    a=input('Podaj poprawną dzielnicę: ')
    
b= input('Podaj rok urodzenia: ')
rok=0
while rok == 0 :
    while type(b) != int :  
        try :   
            b=int(b)
        except ValueError:
            print('Podałeś złą datę urodzenia! Podpowiedź (podaj liczbę)')
            b=input('Podaj poprawną :')
    if b > 2018:
        print('Pomyliłeś się z datą bo takiej jeszcze nie było')
        b=input('Podaj poprawną datę: ')
    elif b < 1910:
        print('Raczej nie masz więcej niż 108 lat')
        b=input('Podaj poprawną datę: ')
    else:
        rok=b
        pass

f=input('Czy szukasz szkoły specjalnej (T/N): ')
while f not in [ 't','n','T','N','nie','tak','Nie','Tak' ]:
    print('Podałeś złą odpowiedz! Podaj T lub N')
    f=input('Czy szukasz szkoły specjalnej (T/N): ')


c=int(2018-float(b))
d=a.upper()

# Pokazuje ile w danej dzielnicy jest dzieci w podanym wieku
print('\n W wieku', c , 'w dzielnicy', d , 'jest ', Szkoły.demografia.at[c,d],'dzieci \n')

#---------------------------------------------------------------------------------------------------------

bez=[]
podana=[]
pobliska=[]         
PobliskieDzielnice=[]   
if f in ('nie','n','N','Nie') :
    if c < 4 :
        print('Pani/Pana dziecko jest za młode na szkołe.')
    elif c < 6 :
        if Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==a].size == 0:
            pass
        else:
            podana.append(Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==a])
        if Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a].size == 0:
            pass
        else:
             podana.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a])
        bez.append(bezp.bezp['PRZEWIDYWANE PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2018 R. (liniowo)'][bezp.bezp['Dzielnica']==a])
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                if Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[0][Szkoły.szkoly[0]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)
                if Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    PobliskieDzielnice.append(i)
                    pobliska.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i])
            bez.append(bezp.bezp['PRZEWIDYWANE PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2018 R. (liniowo)'][bezp.bezp['Dzielnica']==i])
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:')
        for i in range(0,len(podana)):
            for j in range(0,len(podana[i])):
               print(podana[i]['Dzielnica'].index[j], ' ' , podana[i]['Dzielnica'][j])
        print('\n Lub do szkoły w pobliżu :')
        for i in range(0,len(pobliska)):
            for j in range(0,len(pobliska[i])):
                print(pobliska[i]['Dzielnica'].index[j], ' ' , pobliska[i]['Dzielnica'][j])
    elif c < 16 :
        if Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==a].size == 0:
            pass
        else:
            podana.append(Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==a])
        if Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a].size == 0:
            pass
        else:
             podana.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==a])
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                if Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[1][Szkoły.szkoly[1]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)                    
                if Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[2][Szkoły.szkoly[2]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:')
        for i in range(0,len(podana)):
            for j in range(0,len(podana[i])):
                print(podana[i]['Dzielnica'].index[j], ' ' , podana[i]['Dzielnica'][j])
        print('\n Lub do szkoły w pobliżu :')
        for i in range(0,len(pobliska)):
            for j in range(0,len(pobliska[i])):
                print(pobliska[i]['Dzielnica'].index[j], ' ' , pobliska[i]['Dzielnica'][j])
    elif c < 20 :
        if Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==a].size == 0:
            pass
        else:
            podana.append(Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==a])
        if Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==a].size == 0:
            pass
        else:
             podana.append(Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==a])
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                if Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[3][Szkoły.szkoly[3]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)
                if Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[4][Szkoły.szkoly[4]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:')
        for i in range(0,len(podana)):
            for j in range(0,len(podana[i])):
                print(podana[i]['Dzielnica'].index[j], ' ' , podana[i]['Dzielnica'][j])
        print('\n Lub do szkoły w pobliżu :')
        for i in range(0,len(pobliska)):
            for j in range(0,len(pobliska[i])):
                print(pobliska[i]['Dzielnica'].index[j], ' ' , pobliska[i]['Dzielnica'][j])
    else :
        if Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==a].size == 0:
            pass
        else:
            podana.append(Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==a])
        for i in Szkoły.Dzielnice.loc[a,:] :
            if i == None:
                pass #Aby omineło wartoci None
            else:
                if Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==i].size == 0 :
                    pass
                else:
                    pobliska.append(Szkoły.szkoly[5][Szkoły.szkoly[5]['Dzielnica']==i])
                    PobliskieDzielnice.append(i)
        print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:')
        for i in range(0,len(podana)):
            for j in range(0,len(podana[i])):
                print(podana[i]['Dzielnica'].index[j], ' ' , podana[i]['Dzielnica'][j])
        print('\n Lub do szkoły w pobliżu :')
        for i in range(0,len(pobliska)):
            for j in range(0,len(pobliska[i])):
                print(pobliska[i]['Dzielnica'].index[j], ' ' , pobliska[i]['Dzielnica'][j])
else : 
    if Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==a].size == 0:
        pass
    else:
        podana.append(Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==a])     
    for i in Szkoły.Dzielnice.loc[a,:] :
        if i == None:
            pass #Aby omineło wartoci None
        else:
            if Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==i].size == 0 :
                pass
            else:
                pobliska.append(Szkoły.szkoly[6][Szkoły.szkoly[6]['Dzielnica']==i])
                PobliskieDzielnice.append(i)
    print('Pani/Pana dziecko może iść do tych szkół w podanej dzielnicy:')
    for i in range(0,len(podana)):
        for j in range(0,len(podana[i])):
            print(podana[i]['Dzielnica'].index[j], ' ' , podana[i]['Dzielnica'][j])
    print('\n Lub do szkoły w pobliżu :')
    for i in range(0,len(pobliska)):
        for j in range(0,len(pobliska[i])):
            print(pobliska[i]['Dzielnica'].index[j], ' ' , pobliska[i]['Dzielnica'][j])

#------------------------------------------------------------------------------------------

p=input('Czy chcesz porównać bezpieczeństwo w danych dzielnicach? (T/N)')
while f not in [ 't','n','T','N','nie','tak','Nie','Tak' ]:
    print('Podałeś złą odpowiedz! Podaj T lub N')
    p=input('Czy chcesz porównać bezpieczeństwo w danych dzielnicach? (T/N)')
#-------------------------------------------------------------------------------------------
PobliskieDzielnice.append(a)
PobliskieDzielnice=set(PobliskieDzielnice)
if p in ('nie','N','n'):
    print('Dziekujemy za skorzystanie z programu :)')
else:
    print('Przewidywane bezpieczeństwo w dzielnicach na rok 2018. ')
    for i in PobliskieDzielnice:
        print(i,'-', '{0:.2f}'.format(float(bezp.bezp['PRZEWIDYWANE PRZESTĘPSTWA NA 1000 MIESZKAŃCÓW W 2018 R. (liniowo)'][bezp.bezp['Dzielnica']==i])),'przestępstwa na 1000 mieszkańców')
    print('\n Dziekujemy za skorzystanie z programu :)')    
    # "{0:.2f}".format(float(bez)))
