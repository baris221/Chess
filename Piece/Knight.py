# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:50:08 2022

@author: baris
"""

def GetValideHand(game,piece):
    
    MouvPosible=[(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    ValideHand=[]
    
    for mouv in MouvPosible:
        if piece[2]+mouv[0] <=7 and piece[2]+mouv[0] >=0 and piece[3]+mouv[1] <=7 and piece[3]+mouv[1] >=0:
            if game[0][piece[2]+mouv[0]][piece[3]+mouv[1]][0]==0 or game[0][piece[2]+mouv[0]][piece[3]+mouv[1]][0]==(3-piece[0]):
                ValideHand.append([piece[2]+mouv[0],piece[3]+mouv[1]])
    
    return ValideHand