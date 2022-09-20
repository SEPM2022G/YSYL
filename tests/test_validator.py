from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects import Outcome, State
v = Validator()

def init():
    oldstate = State()
    newstate = State()
    result = v.check(oldstate, newstate)
    assert(result == Outcome.VALID)
