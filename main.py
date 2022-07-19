# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:27:32 2022

@author: baris
"""

import Chess

game=Chess.InitialGame()


#Chess.PrintBoard(game[0])
Chess.PrintGame(game)
print("\033[1;0m")

for piece in game[3]:
    Chess.printValideHand(game,piece)
for piece in game[4]:
    Chess.printValideHand(game,piece)
    
def part(game):
    [piece,pos]=Chess.handChoice(game)
    Chess.playHand(game,piece,pos)