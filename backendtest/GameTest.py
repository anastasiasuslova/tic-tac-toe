import unittest
from backend.GameStatus import GameStatus
from backend.Game import Game


class GameTest(unittest.TestCase):


    def testGameStatusNotFinished(self):
        status = GameStatus(0);
        self.assertFalse(status.isGameOver, "");

    def testGameStatusFinished(self):
        status = GameStatus(0);
        status.isGameOver = True;
        self.assertTrue(status.isGameOver, "");

    def testGameIsNotOver(self):
        game = Game(0);
        self.assertFalse(game.checkGameOver());
        self.assertEqual(game.gameStatus.winner, None, "")
                
    def testGameIsOver(self):
        game = Game(0);
        player = 1
        testGrid = [[player] * 5] * 6;        
        game.gameStatus.grid = testGrid;
        self.assertTrue(game.checkGameOver());
        self.assertEqual(game.gameStatus.winner, player, "")
        
    def testGetWinner1(self):
        game = Game(0);
        array = [1] * 5;
        winner = 1       
        self.assertEqual(game.getWinner(array), winner, "")        

    def testGetWinner0(self):
            game = Game(0);
            array = [0] * 5;
            winner = 0       
            self.assertEqual(game.getWinner(array), winner, "")
                        
    def testGetWinnerNone(self):
        game = Game(0);
        array = [1, None, 0, 1, None];
        winner = None       
        self.assertEqual(game.getWinner(array), winner, "")   
        
    def testDiagonaWin(self):
        game = Game(0);       
        testGrid = [[None, 0, 1], [None, 1, 0], [1, None, None]];        
        game.gameStatus.grid = testGrid;
        self.assertTrue(game.checkGameOver());
        self.assertEqual(game.gameStatus.winner, 1, "")
        
    
    
    def testRowWin(self):
        game = Game(0);       
        testGrid = [[0, 1, 0], [0, 1, None], [0, None, None]];      
        game.gameStatus.grid = testGrid;
        self.assertTrue(game.checkGameOver());
        self.assertEqual(game.gameStatus.winner, 0, "")
        
    def testColumnWin(self):     
        game = Game(0);       
        testGrid = [[0, 0, 0], [1, 1, None], [0, None, None]];         
        game.gameStatus.grid = testGrid;
        self.assertTrue(game.checkGameOver());
        self.assertEqual(game.gameStatus.winner, 0, "")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()