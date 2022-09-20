import unittest
import src.GameEngine.Components.IOProcessor as proc
from src.GameEngine.Objects.Move import Move


class TestIO(unittest.TestCase):

    def testinputToMove(self):
        testmove = Move()
        testmove.moveNumber = 5
        testmove.player = 1
        testmove.colour = "white"
        testmove.board = "Test State"
        move = proc.IOProcessor.inputToMove()
        self.assertEqual(testmove.moveNumber, move.moveNumber)
        self.assertEqual(testmove.player, move.player)
        self.assertEqual(testmove.colour, move.colour)
        self.assertEqual(testmove.board, move.board)


if __name__ == '__main__':
    unittest.main()
