from gameObjects import mayGameObject
from gameConsts import *
import pyxel

class mayCoin(mayGameObject):
    def __init__(self, x, y):
        mayGameObject.__init__(self, x, y, TILEOFFSET, TILEOFFSET, True, 0)
        self.incScore = GAME_SCORE_PER_COIN
        self.name = 'coin'
        
    def _update(self):
        pass
    
    def _draw(self):
        pyxel.blt(self.x, self.y, IS_GAME_OBJECT, COIN_X_OFFSET, COIN_Y_OFFSET, self.width, self.height, 1)
        