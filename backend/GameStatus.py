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
        self.xWon = False
        self.xTurn = False
        self.grid = [[None] * numOfColumns] * numOfRows 
        
    
   
    
    
    