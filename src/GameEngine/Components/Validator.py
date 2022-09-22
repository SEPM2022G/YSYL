import numpy as np
from src.GameEngine.Objects.Enums import Orientation, Color
from src.GameEngine.Objects.Outcome import Outcome

class Validator:
    '''
    Validate moves and checks for win condition.
    '''

    def check(self, oldstate, newstate) -> Outcome:
        return Outcome.VALID

    def win_check(self, board) -> Outcome:
        '''
        Checks for a win
        '''
        for y in range(0,5):
            turns = 0
            elem = self._find_top(board[0][y])

            for x in range(0,5):
                next_elem = self._find_top(board[x][y])

                if next_elem == -1 or elem == -1:
                    break

                if elem.get_color() != next_elem.get_color():
                    break

                if elem.get_orientation() != next_elem.get_orientation():
                    break

                if elem.get_color() == Color.WHITE:
                    return Outcome.WIN_WHITE
                else:
                    return Outcome.WIN_BLACK


    def _find_top(self, arr):
        if arr[0] == 0:
            return -1
        for i, elem in enumerate(arr):
            if elem == 0: 
                return arr[i-1]
        return -1


