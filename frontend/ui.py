# -*- coding: utf-8 -*-
u'''
Created on 03.01.2016

@author: sergey
'''

import gtk
import backend.Game
from mainWindow import mainWindow

class tictactoe_ui(object):
    def __init__(self, game):
        self.mainWindow = mainWindow()
        
        self.game = game
        
        self.mainWindow.board_button_click = self.board_button_click
        self.mainWindow.restart_button_click = self.restart_button_click
        
        self.update_board()

    def update_board(self):
        for row in xrange(3):
            for column in xrange(3):
                if self.game.gameStatus.grid[row][column] == backend.Game.Game.X_PLAYER:
                    self.mainWindow.buttons[row][column].set_label("x")
                elif self.game.gameStatus.grid[row][column] == backend.Game.Game.O_PLAYER:
                    self.mainWindow.buttons[row][column].set_label("o")
                else:
                    self.mainWindow.buttons[row][column].set_label("")

    def board_button_click(self, button, field):
        if self.game.makeMove(*field):
            pass
        else:
            self.mainWindow.status_label.set_label("incorrect move")
        self.update_board()
    
    def restart_button_click(self, button):
        pass
    
    def run(self):
        gtk.main()




