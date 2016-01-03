import unittest
from backend.GameStatus import GameStatus
from backend.Game import Game


class GameTest(unittest.TestCase):


    def testGameStatusNotFinished(self):
        status = GameStatus(0);
        self.assertFalse(status.isGameOver, "");

    def testGameStatusFinished(self):
        status = GameStatus(0);
        status.isFinished = True;
        self.assertTrue(status.isGameOver, "");

    def testGameIsNotOver(self):
        game = Game(0);
        self.assertFalse(game.checkGameOver());
                
    def testGameIsOver(self):
        game = Game(0);
        testGrid = [[1] * 5] * 6;        
        game.gameStatus.grid = testGrid;
        self.assertTrue(game.checkGameOver());

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()