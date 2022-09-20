import sys
import unittest
sys.path.append("..")
from src.GameEngine.Components import IOProcessor as proc
from src.GameEngine.Objects import Move


class TestIO(unittest.TestCase):

    def testinputToMove(self):
        testmove = Move()
        testmove.isPile = True
        testmove.srcPos_x = 0
        testmove.srcPos_y = 0
        testmove.destPos_x = 0
        testmove.destPos_y = 0
        testmove.destOrientation = "Orientation.Flat"
        testmove.pieces = 2
        testmove.color = "Color.White"
        testmove.first_turn = False
        IO = proc.IOProcessor()
        move = IO.inputToMove()
        self.assertEqual(testmove.isPile, move.isPile)
        self.assertEqual(testmove.srcPos_x, move.srcPos_x)
        self.assertEqual(testmove.srcPos_y, move.srcPos_y)
        self.assertEqual(testmove.destPos_x, move.destPos_x)
        self.assertEqual(testmove.destPos_y, move.destPos_y)
        self.assertEqual(testmove.destOrientation, move.destOrientation)
        self.assertEqual(testmove.pieces, move.pieces)
        self.assertEqual(testmove.color, move.color)
        self.assertEqual(testmove.first_turn, move.first_turn)


if __name__ == '__main__':
    unittest.main()
