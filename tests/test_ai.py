from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.GameAI import GameAI
from src.GameEngine.Objects.Enums import Color, Orientation

move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 1,
        "pos_y": 1,
        "orientation": Orientation.FLAT
    },
    "pieces": 1,
    "color": Color.BLACK,
    "first_turn": False
}

#print("hejjj")
ai = GameAI("easy")
sm = StateManager()

sm.update_state(move)

move["des"]["pos_x"] = 3
move["des"]["pos_y"] = 2
move["color"] = Color.WHITE
sm.update_state(move)

sm.print_state()
print("################################################################")
print("Score: ",ai.minimax(4, Color.WHITE, sm))
print(ai.best_move)
sm.update_state(ai.best_move)
sm.print_state()