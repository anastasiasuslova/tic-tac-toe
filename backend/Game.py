# -*- coding: utf-8 -*-
u'''
Created on 3 янв. 2016 г.

@author: Nastya
'''

from backend.GameStatus import GameStatus

class Game(object):
    '''
    classdocs
    '''
    X_PLAYER = 1
    O_PLAYER = 0
    


    def __init__(self, params):
        '''
        Constructor
        '''
        self.resetGame()
                
        
    def resetGame(self):
        self.gameStatus = GameStatus(0)
        self.currentPlayer = self.X_PLAYER
        
    def makeMove(self, column, row):
        successful = False
        
        if self.gameStatus.grid[column][row] is not None:
            self.gameStatus.grid[column][row] = self.currentPlayer
            
            if self.currentPlayer == self.X_PLAYER:
                self.currentPlayer = self.O_PLAYER
            else:
                self.currentPlayer = self.X_PLAYER
                 
            successful = True
                
        return successful
    
    
    def checkGameOver(self):
        self.gameStatus.gameIsOver = True
        
        # check all cells filled
        for col in range(len(self.gameStatus.grid)):
            for row in range(len(self.gameStatus.grid[col])):
                if self.gameStatus.grid[col][row] is None:
                    self.gameStatus.gameIsOver = False
                    break
        
        # check all cells in a row, column or diagonal filled by one player
        # columns
        grid1 = self.gameStatus.grid
        for col in range(len(grid1)):            
            a = 0
                
        # rows
        
        # diagonal  
        
        # set winner
        # self.gameStatus.xWon
        
        return self.gameStatus.gameIsOver
    
    