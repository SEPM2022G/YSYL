import numpy as np
from src.GameEngine.Objects.Enums import Orientation, Color
from src.GameEngine.Objects.Outcome import Outcome
outcome = [Outcome.WIN_WHITE, Outcome.WIN_BLACK]


class Validator:
    '''
    Validate moves and checks for win condition.
    '''

    def check(self, move, oldstate, newstate) -> Outcome:
        newboard = newstate["board"]
        oldboard = oldstate["board"]

        des = move["des"]
        src = move["src"]

        win_state = self._win_check(newboard)
        if win_state != Outcome.CONT:
            return win_state

        if move["pieces"] < 1:
            return Outcome.INVALID

        # First round
        if move["first_turn"] and (not src["pile"] or move["pieces"] != 1):
            return Outcome.INVALID

        # des
        if des["pos_x"] < 0 or des["pos_x"] > 4:
            return Outcome.INVALID

        if des["pos_y"] < 0 or des["pos_y"] > 4:
            return Outcome.INVALID

        des_elem = self._find_top(oldboard[des["pos_x"]][des["pos_y"]])
        if des_elem != -1 and des_elem.get_color() != move["color"] and not move["first_turn"]:
            return Outcome.INVALID

        if des_elem != -1 and des_elem.get_orientation() == Orientation.STANDING:
            return Outcome.INVALID

        # src
        if (src["pos_x"] < 0 or src["pos_x"] > 4) and not src["pile"]:
            return Outcome.INVALID

        if (src["pos_y"] < 0 or src["pos_y"] > 4) and not src["pile"]:
            return Outcome.INVALID

        src_elem = self._find_top(oldboard[src["pos_x"]][src["pos_y"]])
        if type(src_elem) != int and (not src["pile"] and src_elem.get_color() != move["color"]):
            return Outcome.INVALID

        if src["pile"] == True and not move["first_turn"]:
            if move["color"] == Color.WHITE and oldstate["white_pieces_pile"] - move["pieces"] < 0:
                return Outcome.INVALID
            if move["color"] == Color.BLACK and oldstate["black_pieces_pile"] - move["pieces"] < 0:
                return Outcome.INVALID

        # Check that n pieces are correct color
        src_stack = oldboard[src["pos_x"]][src["pos_y"]]
        src_stack = src_stack[src_stack != 0]

        for i, elem in enumerate(src_stack[-move["pieces"]:]):
            src_stack[i] = elem.get_color() == move["color"]

        if not src["pile"] and not np.all(src_stack):
            return Outcome.INVALID

        # Prevents idle move
        if src["pos_y"] == des["pos_y"] and src["pos_x"] == des["pos_x"] and src_elem != -1:
            if not src["pile"] and des["orientation"] == src_elem.get_orientation():
                return Outcome.INVALID

        return Outcome.VALID

    def _win_check(self, board) -> Outcome:
        '''
        Checks for a win
        '''
        for y in range(0, 5):

            has_turned = False
            for x in range(1, 5):
                next_elem = self._find_top(board[x][y])
                prev_elem = self._find_top(board[x - 1][y])

                # Checks for valid turning paths
                if prev_elem != -1 and next_elem != prev_elem and not has_turned:
                    has_turned = True
                    path_check = Outcome.CONT

                    if y > 0 and prev_elem == self._find_top(board[x-1][y-1]):
                        path_check = self._check_path(x, y-1, board)
                        if path_check != Outcome.CONT: return path_check

                    if y < 4 and prev_elem == self._find_top(board[x-1][y+1]):
                        path_check = self._check_path(x, y+1, board)
                        if path_check != Outcome.CONT: return path_check

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
