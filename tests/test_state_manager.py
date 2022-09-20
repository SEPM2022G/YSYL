import sys
import unittest
sys.path.append("..") # Adds higher directory to python modules path.
from src.GameEngine.Components import StateManager as SM
from src.GameEngine.Enums import Orientation, Color


move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 0,
        "pos_y": 0,
        "orientation": Orientation.FLAT
    },
    "pieces": 1,
    "color": Color.WHITE,
    "first_turn": False
}


sm = SM.StateManager()

class TestStateManager(unittest.TestCase):

    def test_1_init_condition(self):
        state = sm.get_state()
        self.assertEqual(state["white_pieces_pile"], 21, "Should be 21 white pieces")
        self.assertEqual(state["black_pieces_pile"], 21, "Should be 21 black pieces")
    
    def test_2_piece_from_pile(self):
        state = sm.update_state(move)
        x = move["des"]["pos_x"]
        y = move["des"]["pos_y"]
        self.assertEqual(str(state["board"][x][y][0]), "(WHITE, FLAT)", "Should be a white piece on the board")

    def test_3_piece_on_piece(self):
        state = sm.update_state(move)
        state = sm.update_state(move)
        x = move["des"]["pos_x"]
        y = move["des"]["pos_y"]
        self.assertEqual(str(state["board"][x][y][0]), "(WHITE, FLAT)", "Should be a white piece on top of a white piece")
        self.assertEqual(str(state["board"][x][y][1]), "(WHITE, FLAT)", "Should be a white piece on top of a white piece")

    def test_4_first_turn(self):
        x = move["des"]["pos_x"] = 1 
        y = move["des"]["pos_y"] = 1
        move["first_turn"] = True
        state = sm.update_state(move)
        self.assertEqual(str(state["board"][x][y][0]), "(BLACK, FLAT)", "Should be a black piece instead of a white one")
        move["color"] = Color.BLACK
        state = sm.update_state(move)
        self.assertEqual(str(state["board"][x][y][1]), "(WHITE, FLAT)", "Should be a white piece instead of a black one")
        move["first_turn"] = False
    
    def test_5_move_stack(self):
        move["des"]["pos_x"] = 0
        move["des"]["pos_y"] = 1
        move["color"] = Color.WHITE
        state = sm.update_state(move)
        state = sm.update_state(move)
        state = sm.update_state(move)

        move["src"]["pile"] = False
        move["pieces"] = 2
        src_x = move["src"]["pos_x"] = 0
        src_y = move["src"]["pos_y"] = 1
        des_x = move["des"]["pos_x"] = 0
        des_y = move["des"]["pos_y"] = 2
        state = sm.update_state(move)

        self.assertEqual(str(state["board"][des_x][des_y][0]), "(WHITE, FLAT)", "Should be a white piece")
        self.assertEqual(str(state["board"][des_x][des_y][1]), "(WHITE, FLAT)", "Should be a white piece on top of a white piece")
        self.assertEqual(str(state["board"][src_x][src_y][0]), "(WHITE, FLAT)", "Should be a white piece left on the source")
        self.assertEqual(state["board"][src_x][src_y][1], 0, "Should be empty (0)")
        self.assertEqual(state["board"][src_x][src_y][2], 0, "Should be empty (0)")

if __name__ == '__main__':
    unittest.main()

