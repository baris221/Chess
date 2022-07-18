# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:19:19 2022

@author: baris
"""

#game=[[int,int],int,[int,int],whitepieces,blackpieces]
#game[0]=game board
#game[1]=the player 1 or 2 
#game[2]=The score 
#game[3]=List of white pieces
#game[4]=List of black pieces

#piece=[int,int,int,int]
#piece[0]=the player 1 or 2
#piece[1]=
#########1 for pawns
#########2 for rook
#########3 for knight
#########4 for bishop
#########5 for queen
#########6 for king
#piece[2] and piece[3] are respectively their position in the game on axis x and y


import sys
sys.path.append("..")
import copy

sys.path.append("./Piece")
import Pawn
import Rock
import Bishop
import Knight
import Quenn

def GetCopyGame(game):
    """game -> game
    Return copy of the game"""
    return copy.deepcopy(game)
    
def GetBoard(game):
    """game->List[int][int]
    Return the board of the game"""
    
    return game[0]

def GetPlayer(game):
    """game->int
    Return the player of the game"""
    
    return game[1]

def ChangePlayer(game):
    """game->void
    Change player of the game"""
    
    game[1]=3-game[1]
    
def GetScore(game):
    """game->(int,int)
    Return the score of game
    First is the score of player 1
    Second is the score of player 2"""
    return  game[2]

def GetPlayerScore(game,player):
    """game->int
    Return the score of player in the game """
    return game[2][player-1]

def GetWhitePieceList(game):
    """game->List[piece]
    Return white piece list"""
    return game[3]

def GetBlackPieceList(game):
    """game->List[piece]
    Return black piece list"""
    return game[4]

def GetValuePiece(piece):
    """ Piece -> int
    hypothese: Piece is not king
    Return the value of pieces"""
    IdPiece=piece[1]
    if IdPiece==3 or IdPiece==4:
        return 3
    
    if IdPiece==2:
        return 5
    
    if IdPiece==1:
        return 1
    
    if IdPiece==5:
        return 9

def CreatePiece(Player,IdPiece,x,y):
    return (Player,IdPiece,x,y)

def PlacePiecesBoard(board,InitialWhiteList,InitialBlackList):
    for whitepiece in InitialWhiteList:
        board[whitepiece[2]][whitepiece[3]]=[whitepiece[0],whitepiece[1]]
        
    for blackpiece in InitialBlackList:
        board[blackpiece[2]][blackpiece[3]]=[blackpiece[0],blackpiece[1]]
    
    

    
def WhiteInitialListe():
    ListPiece=[]
    for i in range(8):
        ListPiece.append(CreatePiece(1,1,1,i))
    for j in range(0,8,7):
        ListPiece.append(CreatePiece(1,2,0,j))
    for m in range(1,7,5):
        ListPiece.append(CreatePiece(1,3,0,m))
    for n in range(2,6,3):
        ListPiece.append(CreatePiece(1,4,0,n))
    ListPiece.append(CreatePiece(1,5,0,3))
    ListPiece.append(CreatePiece(1,6,0,4))
    
    return ListPiece

def BlackInitialListe():
    ListPiece=[]
    for i in range(8):
        ListPiece.append(CreatePiece(2,1,6,i))
    for j in range(0,8,7):
        ListPiece.append(CreatePiece(2,2,7,j))
    for m in range(1,7,5):
        ListPiece.append(CreatePiece(2,3,7,m))
    for n in range(2,6,3):
        ListPiece.append(CreatePiece(2,4,7,n))
    
    ListPiece.append(CreatePiece(2,5,7,3))
    ListPiece.append(CreatePiece(2,6,7,4))
    
    return ListPiece

def InitialGame():
    game=[]   
    #initial game table without pieces
    board=[]
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append([0,0])
    #Place the pieces
    game.append(board)
    
    #Player
    game.append(1)
    
    #Score
    game.append([0,0])
    
    #White List
    game.append(WhiteInitialListe())
    
    #Black List
    game.append(BlackInitialListe())
    PlacePiecesBoard(board,game[3],game[4])
    
    return game

def PiecePrint(Piece):
    if Piece==1:
        return 'P'
    
    if Piece==2:
        return "R"
    if Piece==3:
        return "N"
    if Piece==4:
        return "B"
    if Piece==5:
        return "Q"
    
    if Piece==6:
        return "K"
    
    return " "

def PrintBoard(board):
    Lettre=["A","B","C","D","E","F","G","H"]
    print("  ",end="")
    for l in Lettre:
        print("| {} ".format(l), end='')
    print('|')

    for i in range(8):
        print("\033[1;0m---",end="")
        for j in range(8):
            print("\033[1;0m----",end="")
        print("")
        
        print("\033[1;0m{} |".format(i+1), end='')
        for m in range(8):
            if board[i][m][1] != 0:
                if board[i][m][0]==1:
                    print("\033[1;0m {} |".format(PiecePrint(board[i][m][1])),end ='')
                else:
                    print("\033[1;30m {} |".format(PiecePrint(board[i][m][1])),end ='')
            else:
                print("\033[1;0m {} |".format(" "),end ='')
        
        print("")
  
def PrintGame(game):
    print("The turn of player {}".format(game[1]))
    print("First player score is {}".format(game[2][0]))
    print("Second player score is {}".format(game[2][1]))
    
    PrintBoard(game[0])

def GetValideHand(game,piece):
    #print(piece)
    if piece[1]==1:
        return Pawn.GetValideHand(game,piece)
    if piece[1]==2:
        return Rock.GetValideHand(game, piece)
    if piece[1]==3:
        return Knight.GetValideHand(game, piece)
    if piece[1]==4:
        return Bishop.GetValideHand(game, piece)
    if piece[1]==5:
        return Quenn.GetValideHand(game, piece)
    return []
def printValideHand(game,piece):
    Lettre=["A","B","C","D","E","F","G","H"]
    Number=[1,2,3,4,5,6,7,8]
    P=["Pawn","Rock","Knight","Bishop","Quenn","King"]
    print(f'The piece is {P[piece[1]-1]} on {Lettre[piece[2]]}{Number[piece[3]]}')
    for pos in GetValideHand(game, piece):
        print(f'You can play your piece on {Lettre[pos[0]]}{Number[pos[1]]}')

def playHand(game,piece,pos):
    game[5-piece[0]].remove(piece)
    newpiece=CreatePiece(piece[0],piece[1],pos[0],pos[1])
    game[5-piece[0]].append(newpiece)
    