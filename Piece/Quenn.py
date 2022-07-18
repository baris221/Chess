# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:28:57 2022

@author: baris
"""

def GetValideHand(game,piece):
    ValideHand=[]
    for i in range(1,7):
        if (piece[2]+i)<=7:
            if game[0][piece[2]+i][piece[3]][0]==0:
                ValideHand.append([piece[2]+i,piece[3]])
            if game[0][piece[2]+i][piece[3]][0]==(3-piece[0]):
                ValideHand.append([piece[2]+i,piece[3]])
                break
            if game[0][piece[2]+i][piece[3]][0]==piece[0]:
                break
                
    for j in range(1,7):
        if (piece[2]-j)>=0:
            if game[0][piece[2]-j][piece[3]][0]==0:
                ValideHand.append([piece[2]-j,piece[3]])
            if game[0][piece[2]-j][piece[3]][0]==(3-piece[0]):
                ValideHand.append([piece[2]-j,piece[3]])
                break
            if game[0][piece[2]-j][piece[3]][0]==piece[0]:
                break
            
            
    for k in range(1,7):
        if(piece[3]+k)<7:
            if game[0][piece[2]][piece[3]+k][0]==0:
                ValideHand.append([[piece[2]],[piece[3]+k]])
            if game[0][piece[2]][piece[3]+k][0]==(3-piece[0]):
                ValideHand.append([[piece[2]],[piece[3]+k]])
                break
            if game[0][piece[2]][piece[3]+k][0]==piece[0]:
                break
    
    for l in range(1,7):
        if(piece[3]-l)>0:
            if game[0][piece[2]][piece[3]-l][0]==0:
                ValideHand.append([piece[2],piece[3]-l])
            if game[0][piece[2]][piece[3]-l][0]==(3-piece[0]):
                ValideHand.append([piece[2],piece[3]-l])
                break
            if game[0][piece[2]][piece[3]-l][0]==piece[0]:
                break
    for i in range(7):
        if (piece[2]+i<=7) and (piece[3]+i<=7):
            if game[0][piece[2]+i][piece[3]+i][0]==0:
                ValideHand.append([piece[2]+i,piece[3]+i])
            
            if game[0][piece[2]+i][piece[3]+i][0]==(3-piece[0]):
                ValideHand.append([piece[2]+i,piece[3]+i])
                break
            if game[0][piece[2]+i][piece[3]+i][0]==piece[0]:
                break
    #Upper left       
    for j in range(7):
        if(piece[2]+j<=7) and (piece[3]-j>=0):
            if game[0][piece[2]+j][piece[3]-j][0]==0:
                ValideHand.append([piece[2]+j,piece[3]-j])
            if game[0][piece[2]+j][piece[3]-j][0]==(3-piece[0]):
                ValideHand.append([piece[2]+j,piece[3]-j])
                break
            if game[0][piece[2]+j][piece[3]-j][0]==piece[0]:
                break
            
    #Down right
    for k in range(7):
        if(piece[2]-k>=0) and (piece[3]+k<=7):
            if game[0][piece[2]-k][piece[3]+k<7][0]==0:
                ValideHand.append([piece[2]-k,piece[3]+k])
            if game[0][piece[2]-k][piece[3]+k<7][0]==(3-piece[0]):
                ValideHand.append([piece[2]-k,piece[3]+k])  
                break            
            if game[0][piece[2]-k][piece[3]+k<7][0]==piece[0]:
                break
            
    for l in range(7):
        if (piece[2]-l>=0) and (piece[3]-l>=0):
            if game[0][piece[2]-l][piece[3]-l][0]==0:
                ValideHand.append(piece[2]-l,piece[3]-l)
            if game[0][piece[2]-l][piece[3]-l][0]==(3-piece[0]):
                ValideHand.append(piece[2]-l,piece[3]-l)   
                break
            if game[0][piece[2]-l][piece[3]-l][0]==piece[0]:
                break
    
    return ValideHand