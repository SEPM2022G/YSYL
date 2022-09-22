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
        outcome = [ Outcome.WIN_WHITE, Outcome.WIN_BLACK ]
        for y in range(0,5):

            cont = True
            for x in range(1,5):
                next_elem = self._find_top(board[x][y])
                prev_elem = self._find_top(board[x - 1][y])

                if next_elem == -1 or prev_elem == -1:
                    break
                if next_elem.get_color() != prev_elem.get_color():
                    break
                if next_elem.get_orientation() != prev_elem.get_orientation():
                    break
            else:
                return outcome[prev_elem.get_color().value]

        return Outcome.CONT


    def _find_top(self, arr):
        if arr[0] == 0:
            return -1
        for i, elem in enumerate(arr):
            if elem == 0: 
                return arr[i-1]
        return -1


