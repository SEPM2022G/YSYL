from enum import Enum

class Outcome(Enum):
    '''
    represents a 'Outcome' object that can be passed between validator,
    controller and state manager components
    '''
    INVALID = 0
    VALID = 1
    WIN_WHITE = 2
    WIN_BLACK = 3
