'''
Created on 03.01.2016

@author: sergey
'''

import backend.Game
import frontend.ui

def main():
    game = backend.Game.Game(None)
    ui = frontend.ui.tictactoe_ui(game)
    ui.run()

if __name__ == '__main__':
    main()