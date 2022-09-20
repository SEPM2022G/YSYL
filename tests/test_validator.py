from src.GameEngine.Components.Validator import Validator
from src.GameEngine.Objects.State import State
from src.GameEngine.Objects.Outcome import Outcome
v = Validator()

# Init
def test_init():
    oldstate = State()
    newstate = State()
    result = v.check(oldstate, newstate)
    assert(result == Outcome.VALID)
