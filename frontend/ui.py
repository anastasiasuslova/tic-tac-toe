# -*- coding: utf-8 -*-
u'''
Created on 03.01.2016

@author: sergey
'''

import pygtk
import gtk
import backend.Game

class tictactoe_ui(object):
    def __init__(self, game):
        self.mainWindow = mainWindow()
        
        self.game = game
        
        self.mainWindow.board_button_click = self.board_button_click
        self.mainWindow.restart_button_click = self.restart_button_click

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

class mainWindow(object):
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", gtk.main_quit)
        self.window.set_title("Tic-Tac-Toe")
        
        vbox = gtk.VBox(spacing = 4)
        self.window.add(vbox)
        
        hbox = gtk.HBox(spacing = 4)
        vbox.pack_start(hbox)
        
        frame = gtk.Frame("")
        label = gtk.Label("Game state here")
        self.status_label = label
        frame.add(label)        
        hbox.pack_start(frame)
        
        button = gtk.Button("Restart")
        button.connect("clicked", self._restart_button_click)
        hbox.pack_start(button)
        
        board = self.make_board()
        vbox.pack_start(board)
        
        self.window.show_all()
    
    def make_board(self):
        table = gtk.Table(rows=3, columns=3)
        self.buttons = [[0 for i in xrange(3)] for i in xrange(3)]
        for row in xrange(3):
            for column in xrange(3):
                button = gtk.Button("X")
                self.buttons[row][column] = button 
                button.connect("clicked", self._board_button_click, (row, column))
                table.attach(button, row, row+1, column, column+1)
        return table
    
    def _board_button_click(self, button, field):
        self.board_button_click(button, field)
        
    def board_button_click(self, button, field):
        raise Exception("Should be overridden")
    
    def _restart_button_click(self, button):
        self.restart_button_click(button)
        
    def restart_button_click(self, button):
        raise Exception("Should be overridden")
    
def main():
    mainWindow()
    gtk.main()
    return 0

if __name__ == "__main__":
    main()


