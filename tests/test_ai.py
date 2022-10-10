from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.Components.MoveController import MoveController
from src.GameEngine.Objects.Enums import Color, Orientation, Difficulty
import sys

# #def easy_test_integration():
# print("#AI EASY TESTTT######################################################")
# sm = StateManager()
# ai = MoveController(sm, Difficulty.EASY, Color.WHITE)

# move = {
#     "src": {
#         "pile": True,
#         "pos_x": 1,
#         "pos_y": 1,
#     },
#     "des": {
#         "pos_x": 1,
#         "pos_y": 1,
#         "orientation": Orientation.STANDING
#     },
#     "pieces": 1,
#     "color": Color.BLACK,
#     "first_turn": False
# }

# sm.update_state(move)
# print("#BOARD BEFORE AI MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

# move["des"]["pos_x"] = 0
# sm.update_state(move)
# print("#BOARD BEFORE AI MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

# print()
# print("#AI MEDIUM TESTTT######################################################")
# sm = StateManager()
# ai = MoveController(sm, Difficulty.MEDIUM, Color.WHITE)

# move = {
#     "src": {
#         "pile": True,
#         "pos_x": 1,
#         "pos_y": 1,
#     },
#     "des": {
#         "pos_x": 1,
#         "pos_y": 1,
#         "orientation": Orientation.STANDING
#     },
#     "pieces": 1,
#     "color": Color.BLACK,
#     "first_turn": False
# }

# sm.update_state(move)
# print("#BOARD BEFORE AI RANDOM MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI RANDOM MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

# move["des"]["pos_x"] = 0
# sm.update_state(move)
# print("#BOARD BEFORE AI BEST MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI BEST MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

# #def hard_test_integration():
# print()
# print("#AI WIN HARD TESTTT######################################################")

# move = {
#     "src": {
#         "pile": True,
#         "pos_x": 1,
#         "pos_y": 1,
#     },
#     "des": {
#         "pos_x": 0,
#         "pos_y": 1,
#         "orientation": Orientation.STANDING
#     },
#     "pieces": 1,
#     "color": Color.WHITE,
#     "first_turn": False
# }

# sm = StateManager()
# ai = MoveController(sm, Difficulty.HARD, Color.WHITE)

# move["des"]["pos_x"] = 0
# sm.update_state(move)
# move["des"]["pos_x"] = 1
# sm.update_state(move)
# move["des"]["pos_x"] = 2
# sm.update_state(move)
# move["des"]["pos_x"] = 3
# sm.update_state(move)
# print()
# print("#BOARD BEFORE AI MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

# print()
# print("#AI BEST MOVE HARD TESTTT######################################################")
# sm = StateManager()
# ai = MoveController(sm, Difficulty.HARD, Color.WHITE)

# move["des"]["pos_x"] = 0
# sm.update_state(move)
# move["des"]["pos_x"] = 2
# sm.update_state(move)
# move["des"]["pos_x"] = 3
# sm.update_state(move)

# move["color"] = Color.BLACK
# move["des"]["pos_y"] = 3
# move["des"]["pos_x"] = 0
# sm.update_state(move)
# move["des"]["pos_x"] = 1
# sm.update_state(move)
# move["des"]["pos_x"] = 2
# sm.update_state(move)
# move["des"]["pos_x"] = 3
# sm.update_state(move)

# print()
# print("#BOARD BEFORE AI MOVE#")
# sm.print_state()
# print("#BOARD AFTER AI MOVE#")
# sm.update_state(ai.move())
# sm.print_state()

print()
print("#AI CORNER TEST######################################################")
sm = StateManager()
ai = MoveController(sm, Difficulty.HARD, Color.WHITE)

move = {
    "src": {
        "pile": True,
        "pos_x": 1,
        "pos_y": 1,
    },
    "des": {
        "pos_x": 4,
        "pos_y": 4,
        "orientation": Orientation.FLAT
    },
    "pieces": 1,
    "color": Color.BLACK,
    "first_turn": False
}

sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
sm.update_state(ai.move())
sm.print_state()
sm.update_state(move)
m = ai.move()
sm.update_state(m)
print(m)
sm.print_state()





