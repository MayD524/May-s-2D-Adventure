from gameEntity import mayGameEntity
import pyxel

class player(mayGameEntity):
    def __init__(self, x:int, y:int, w:int, h:int, p_health:int) -> None:
        mayGameEntity.__init__(self, x, y, w, h, None, p_health)
        
    def _update(self) -> None:
        ## move the player
        if pyxel.btn(pyxel.KEY_LEFT):
            self.move(-1, 0)
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move(1, 0)
            
        if pyxel.btn(pyxel.KEY_SPACE) and not self.in_air:
            self.move(0, -10)
            
        #if pyxel.btn(pyxel.KEY_DOWN):
        #    self.move(0, 1)
        
        if self.in_air:
            self.fall()
        ## handle actions
        
    def _draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height, 0)