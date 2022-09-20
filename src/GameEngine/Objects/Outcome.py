from enum import Enum

class Outcome(Enum):
    '''
    represents a 'Outcome' object that can be passed between validator,
    controller and state manager components
    '''
    INVALID = 0
    VALID = 1
    WIN_PLAYER = 2
    WIN_AI = 3
