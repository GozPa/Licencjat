# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 14:54:43 2018

@author: Paulina
"""
def Toint(b):
    while type(b) is not int:
        try :   
            b=int(b)
        except ValueError:
            print('Podałe złą datę urodzenia!')
            b=input('Podaj poprawną :')
