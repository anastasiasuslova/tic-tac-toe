u'''
Created on 3 янв. 2016 г.

@author: Nastya
'''

from backend.GameStatus import GameStatus

class Game(object):
    '''
    classdocs
    '''
    xPlayer = 1
    oPlayer = 0
    currentPlayer = xPlayer


    def __init__(self, params):
        '''
        Constructor
        '''
        self.gameStatus = GameStatus(0)
                
        
    def makeMove(self, column, row):
        successful = False
        
        if self.gameStatus.grid[column][row] is not None:
            self.gameStatus.grid[column][row] = self.currentPlayer
            
            if self.currentPlayer == self.xPlayer:
                self.currentPlayer = self.oPlayer
            else:
                self.currentPlayer = self.xPlayer
                 
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
        
        # check three cells in a row filled by one player
        
        
        return self.gameStatus.gameIsOver