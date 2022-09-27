from src.GameEngine.Components.StateManager import StateManager
from src.GameEngine.GameAI import GameAI
from src.GameEngine.Objects.Enums import Color

print("hejjj")
ai = GameAI("easy")
sm = StateManager()
ai.minimax(4, Color.WHITE, sm)
print(ai.best_move)