import numpy as np
from src.GameEngine.Objects.Enums import Orientation, Color
from src.GameEngine.Objects.Outcome import Outcome
outcome = [ Outcome.WIN_WHITE, Outcome.WIN_BLACK ]

class Validator:
    '''
    Validate moves and checks for win condition.
    '''

    def check(self, move, state) -> Outcome:
        return Outcome.VALID

    def _win_check(self, board) -> Outcome:
        '''
        Checks for a win
        '''
        for y in range(0,5):

            has_turned = False
            for x in range(1,5):
                next_elem = self._find_top(board[x][y])
                prev_elem = self._find_top(board[x - 1][y])

                # Checks for valid turning paths
                if prev_elem != -1 and next_elem != prev_elem and has_turned == False:
                    has_turned = True
                    path_check = Outcome.CONT

                    if y > 0:
                        prev_down = self._find_top(board[x-1][y-1])
                        if prev_elem == prev_down: path_check = self._check_path(x, y-1, board)
                            
                    if y < 4:
                        prev_top = self._find_top(board[x-1][y+1])
                        if prev_elem == prev_top: path_check = self._check_path(x, y+1, board)

                    if path_check != Outcome.CONT:
                        return path_check
                    
                if next_elem != prev_elem or prev_elem == -1:
                    break
            else:
                return outcome[prev_elem.get_color().value]

        return Outcome.CONT

    def _check_path(self, x, y, board) -> Outcome:
        '''
        Helper function for checking outcomes in straight paths
        '''
        for i in range(x, 5):
            next_elem = self._find_top(board[x][y])
            prev_elem = self._find_top(board[x - 1][y])

            if next_elem != prev_elem or prev_elem == -1:
                return Outcome.CONT
        else:
            return outcome[prev_elem.get_color().value]

    def _find_top(self, arr):
        '''
        Helper function for getting the top piece in a stack
        '''
        if arr[0] == 0:
            return -1
        for i, elem in enumerate(arr):
            if elem == 0: 
                return arr[i-1]
        return -1


