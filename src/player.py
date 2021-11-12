from gameConsts import *
from gameEntity import mayGameEntity
import pyxel

class player(mayGameEntity):
    def __init__(self, x:int, y:int, w:int, h:int, p_health:int) -> None:
        mayGameEntity.__init__(self, x, y, w, h, None, p_health)
        self.name = 'player'
        self.direction = DIRECTION_FRONT
        
    def _update(self) -> None:
        ## move the player
        if pyxel.btn(pyxel.KEY_UP):
            self.direction = DIRECTION_FRONT
        
        if pyxel.btn(pyxel.KEY_LEFT):
            self.move(-1, 0)
            self.direction = DIRECTION_LEFT
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move(1, 0)
            self.direction = DIRECTION_RIGHT
            
        if pyxel.btn(pyxel.KEY_SPACE) and not self.in_air:
            self._jump(20)
        
        if pyxel.btn(pyxel.KEY_DOWN):
            self.direction = MAKE_BLOB_SMALL
        
        if self.in_air and not self.jump:
            self.fall()
            
        elif self.yMove != 0:
            self.move(0, -1.5)
            self.yMove -= 1
            if self.yMove == 0:
                self.jump = False
        ## handle actions
        
    def _draw(self):
        tileXOffSet = 0
        tileYOffSet = 0
        if self.direction == DIRECTION_LEFT:
            #tileXOffSet = TILEOFFSET
            tileYOffSet = TILEOFFSET
        
        elif self.direction == DIRECTION_RIGHT:
            tileXOffSet = TILEOFFSET    
        
        elif self.direction == MAKE_BLOB_SMALL:
            tileXOffSet = TILEOFFSET
            tileYOffSet = TILEOFFSET
        
        pyxel.blt(self.x, self.y, 0, tileXOffSet, tileYOffSet, TILEOFFSET, TILEOFFSET, 2)
        #pyxel.rect(self.x, self.y, self.width, self.height, 7)