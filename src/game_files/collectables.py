from game_files.gameObjects import mayGameObject
from game_files.gameConsts import *
import pyxel

class mayCoin(mayGameObject):
    def __init__(self, x, y):
        mayGameObject.__init__(self, x, y, TILEOFFSET, TILEOFFSET, True, 0)
        self.incScore = GAME_SCORE_PER_COIN
        self.name = 'coin'
        
    def _update(self):
        pass
    
    def _draw(self):
        pyxel.blt(self.x, self.y, IS_GAME_OBJECT, COIN_X_OFFSET, COIN_Y_OFFSET, self.width, self.height, 0)
        
class mayLevelEnd(mayGameObject):
    def __init__(self, x, y):
        mayGameObject.__init__(self, x, y, TILEOFFSET, TILEOFFSET, True, 0)
        self.name = 'level_end'
    
    def _draw(self):
        pyxel.blt(self.x, self.y, IS_GAME_OBJECT, LEVEL_END_X_OFFSET, LEVEL_END_Y_OFFSET, self.width, self.height, 0)
          
class mayHealthKit(mayGameObject):
    def __init__(self, x, y):
        mayGameObject.__init__(self, x, y, TILEOFFSET, TILEOFFSET, True, 0)
        self.name = 'healthKit'
        self.health_inc = 10
        
    def _draw(self):
        pyxel.blt(self.x, self.y, IS_GAME_OBJECT, HEALTH_KIT_X_OFFSET, HEALTH_KIT_Y_OFFSET, self.width, self.height, 0)