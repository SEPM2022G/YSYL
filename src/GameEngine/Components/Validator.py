from src.GameEngine.Objects.Outcome import Outcome


class Validator:

    '''
    Validate moves and checks for win condition.
    '''

    def check(self, oldstate, newstate) -> Outcome:
        return Outcome.VALID

    def _win_check(self, oldstate, newstate) -> bool:
        return False
