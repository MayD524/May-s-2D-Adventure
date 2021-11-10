from gameObjects import mayGameObject
import pyxel

class mayFloor(mayGameObject):
    def __init__(self, x, y, width:int=200, height:int=50):
        mayGameObject.__init__(self, x, y, width, height, True, 0)
        self.name = "floor"
        
    def _update(self):
        pass
    
    def _draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 10)