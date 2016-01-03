u'''
Created on 03.01.2016

@author: sergey
'''

import pygtk
import gtk

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
        frame.add(label)        
        hbox.pack_start(frame)
        
        button = gtk.Button("Restart")
        hbox.pack_start(button)
        
        board = self.make_board()
        vbox.pack_start(board)
        
        self.window.show_all()
    
    def make_board(self):
        table = gtk.Table(rows=3, columns=3)
        for row in xrange(3):
            for column in xrange(3):
                button = gtk.Button("X")
                table.attach(button, row, row+1, column, column+1)
        return table

def main():
    mainWindow()
    gtk.main()
    return 0

if __name__ == "__main__":
    main()


