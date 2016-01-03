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
        self.window.show_all()

def main():
    mainWindow()
    gtk.main()
    return 0

if __name__ == "__main__":
    main()


