# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:17:19 2022

@author: baris
"""
import Chess

def handChoice(game):
    Lettre={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    a=input("Please choose your column :")
    col=Lettre[a]
    lin=int(input("Please choose your line:"))-1
    for p in game[2+game[1]]:
        if p[0]==col and p[1]==lin:
            piece=p
            break
    Chess.printValideHand(game,piece)