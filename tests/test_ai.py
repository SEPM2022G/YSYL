from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.GameAI import GameAI
from src.GameEngine.Objects.Enums import Color, Orientation, Difficulty

#def easy_test_integration():
sm = StateManager()
ai = GameAI(sm, Difficulty.EASY, Color.WHITE)

move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 1,
        "pos_y": 1,
        "orientation": Orientation.STANDING
    },
    "pieces": 1,
    "color": Color.BLACK,
    "first_turn": False
}

sm.update_state(move)
sm.print_state()
sm.update_state(ai.move())
sm.print_state()

move["des"]["pos_x"] = 0
sm.update_state(move)
sm.print_state()
sm.update_state(ai.move())
sm.print_state()
#move[""]
#sm.update_state(move)

#def hard_test_integration():
move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 0,
        "pos_y": 1,
        "orientation": Orientation.STANDING
    },
    "pieces": 1,
    "color": Color.WHITE,
    "first_turn": False
}

print("#AI WIN HARD TESTTT######################################################")
sm = StateManager()
ai = GameAI(sm, Difficulty.HARD, Color.WHITE)

move["des"]["pos_x"] = 0
sm.update_state(move)
move["des"]["pos_x"] = 1
sm.update_state(move)
move["des"]["pos_x"] = 2
sm.update_state(move)
move["des"]["pos_x"] = 3
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()

print("#AI WIN HARD TESTTT######################################################")

print("#AI BEST MOVE HARD TESTTT######################################################")
sm = StateManager()
ai = GameAI(sm, Difficulty.HARD, Color.WHITE)

move["des"]["pos_x"] = 0
sm.update_state(move)
move["des"]["pos_x"] = 2
sm.update_state(move)
move["des"]["pos_x"] = 3
sm.update_state(move)

move["color"] = Color.BLACK
move["des"]["pos_y"] = 3
move["des"]["pos_x"] = 0
sm.update_state(move)
move["des"]["pos_x"] = 1
sm.update_state(move)
move["des"]["pos_x"] = 2
sm.update_state(move)
move["des"]["pos_x"] = 3
sm.update_state(move)

sm.update_state(ai.move())
sm.print_state()

print("#AI BEST MOVE HARD TESTTT######################################################")




