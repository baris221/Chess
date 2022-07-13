# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:27:32 2022

@author: baris
"""

import Chess

game=Chess.InitialGame()
#print(game[4])

#Chess.PrintBoard(game[0])
#Chess.PrintGame(game)

for piece in game[3]:
    print(Chess.GetValideHand(game,piece))
    
for piece in game[4]:
    print(Chess.GetValideHand(game,piece))
    
