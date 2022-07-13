# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:16:11 2022

@author: baris
"""


def GetValideHand(game,piece):
    
    ValideHand=[]
    #print(game[0][piece[3]][piece[2]])
    #White turns
    if(piece[0]==1):
        if(piece[2]<7):           
           if(game[0][piece[2]+1][piece[3]]==0):
              ValideHand.append([piece[2]+1,piece[3]])
              
        if(piece[2]==1 and game[0][piece[2]+2][piece[3]]==0 and game[0][piece[2]+1][piece[3]]==0):
              ValideHand.append([piece[2]+2,piece[3]])
              
        for black in game[4]:
            if (black[2]==piece[2]+1 and black[3]==piece[3]+1) or (black[2]==piece[2]-1 and black[3]==piece[3]+1) :
                ValideHand.append([black[2],black[3]])
    
    #Black turns 
    if(piece[0]==2):
        if(piece[2]>0):
            if(game[0][piece[2]-1][piece[3]]==0):
                ValideHand.append([piece[2]-1,piece[3]])
                
            if(piece[2]==6 and game[0][piece[2]-2][piece[3]]==0 and game[0][piece[2]-1][piece[3]]==0):
                ValideHand.append([piece[2]-2,piece[3]])
                
            for white in game[3]:
                if((white[2]==piece[2]-1 and white[3]==piece[3]-1) or (white[2]==piece[2]-1 and white[3]==piece[3]+1)):
                    ValideHand.append(white[2],white[3])
    
    return ValideHand
                    
def Promote(piece,idpiece):
    """We suppose that piece[3] is equal to 7 for white and is equal to 0 for black
    idpice must be different than 1"""
    piece[1]=idpiece