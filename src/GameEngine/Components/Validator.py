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

            hasTurned = False
            for x in range(1,5):
                next_elem = self._find_top(board[x][y])
                prev_elem = self._find_top(board[x - 1][y])

                if prev_elem != -1 and next_elem != prev_elem and hasTurned == False:
                    hasTurned = True

                    if y > 0:
                        elem_down = self._find_top(board[x][y-1])
                        prev_down = self._find_top(board[x-1][y-1])
                        if elem_down == prev_down and prev_elem == elem_down:
                            y = y - 1 
                            continue

                    if y < 4:
                        elem_top = self._find_top(board[x][y+1])
                        prev_top = self._find_top(board[x-1][y+1])
                        if elem_top == prev_top and prev_elem == elem_top:
                            y = y + 1
                            continue
                
                if next_elem != prev_elem or prev_elem == -1:
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


