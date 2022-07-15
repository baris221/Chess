# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 09:54:10 2022

@author: baris
"""

def GetValideHand(game,piece):
    ValideHand=[]
    
    #Upper right
    for i in range(7):
        if (piece[2]+i<=7) and (piece[3]+i<=7):
            if game[0][piece[2]+i][piece[3]+i]==0:
                ValideHand.append([piece[2]+i,piece[3]+i])
            
            if game[0][piece[2]+i][piece[3]+i]==(3-piece[0]):
                ValideHand.append([piece[2]+i,piece[3]+i])
                break
            if game[0][piece[2]+i][piece[3]+i]==piece[0]:
                break
    #Upper left       
    for j in range(7):
        if(piece[2]+j<=7) and (piece[3]-j>=0):
            if game[0][piece[2]+j][piece[3]-j]==0:
                ValideHand.append([piece[2]+j,piece[3]-j])
            if game[0][piece[2]+j][piece[3]-j]==(3-piece[0]):
                ValideHand.append([piece[2]+j,piece[3]-j])
                break
            if game[0][piece[2]+j][piece[3]-j]==piece[0]:
                break
            
    #Down right
    for k in range(7):
        if(piece[2]-k>=0) and (piece[3]+k<=7):
            if game[0][piece[2]-k][piece[3]+k<7]==0:
                ValideHand.append([piece[2]-k,piece[3]+k])
            if game[0][piece[2]-k][piece[3]+k<7]==(3-piece[0]):
                ValideHand.append([piece[2]-k,piece[3]+k])  
                break            
            if game[0][piece[2]-k][piece[3]+k<7]==piece[0]:
                break
            
    for l in range(7):
        if (piece[2]-l>=0) and (piece[3]-l>=0):
            if game[0][piece[2]-l][piece[3]-l]==0:
                ValideHand.append(piece[2]-l,piece[3]-l)
            if game[0][piece[2]-l][piece[3]-l]==(3-piece[0]):
                ValideHand.append(piece[2]-l,piece[3]-l)   
                break
            if game[0][piece[2]-l][piece[3]-l]==piece[0]:
                break
    
    return ValideHand
            
            
        