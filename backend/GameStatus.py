# -*- coding: utf-8 -*-
u'''
Created on 3 янв. 2016 г.

@author: Nastya
'''

class GameStatus(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        numOfRows = 3
        numOfColumns = numOfRows
        
        self.isGameOver = False
        self.winner = None
        self.xTurn = False # todo rename to current player
        self.grid = [[None for i in range(numOfRows)] for j in range(numOfColumns)]
        
    
   
    
    
    