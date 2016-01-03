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
        
        if self.gameStatus.grid[column][row] is None:
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
        for col in self.gameStatus.grid:            
            self.gameStatus.winner = self.getWinner(col)
            
            if self.gameStatus.winner is not None:
                self.gameStatus.isGameOver = True
                break # end loop
                
        numOfCols = len(self.gameStatus.grid)
        numOfRows = len(self.gameStatus.grid[0])
        # rows
        if self.gameStatus.winner is None:            
            for i in range(numOfRows):
                row = [] * numOfRows
                for j in range(numOfCols):                    
                    row.append(self.gameStatus.grid[j][i])
                    self.gameStatus.winner = self.getWinner(row)
                
            
        
        # diagonal top left to bottom right
        if self.gameStatus.winner is None:      
            diagonal1 = [] * numOfCols
            i = 0
            j = 0
            while i < numOfCols:
                while j < numOfRows:
                    diagonal1.append(self.gameStatus.grid[i][j])
                    i += 1
                    j += 1
            self.gameStatus.winner = self.getWinner(diagonal1)
            
        # diagonal top right to bottom left
        if self.gameStatus.winner is None:      
            diagonal2 = [] * numOfCols
            i = numOfCols
            j = numOfRows
            while i >= 0:
                while j >= 0 :
                    diagonal1.append(self.gameStatus.grid[i][j])
                    i -= 1
                    j -= 1
            self.gameStatus.winner = self.getWinner(diagonal2)
            
        if self.gameStatus.winner is not None:
                self.gameStatus.isGameOver = True
        
        return self.gameStatus.gameIsOver
    
    def getWinner(self, array):
        winner = None
        arraySize = len(array)
        counter = 1
        for i in range(arraySize):            
            if (array[i] is not None) and (i > 0) and (array[i] == array[i-1]):
                counter += 1
                
        if counter == arraySize:
            winner = array[0]
            
        return winner