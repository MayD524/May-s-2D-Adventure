from gameConsts import *
import pyxel
import math

class mayGameObject:
    def __init__(self, x:int, y:int, w:int, h:int, has_col:bool, damageOnCol:int) -> None:
        self.x          = x
        self.y          = y
        self.width      = w
        self.height     = h
        self.has_col    = has_col
        self.dmg        = damageOnCol
        self.speed      = DEFAULT_SPEED
        self.isAlive    = True
        self.canMove    = False
        self.name       = "mayGameObject"
        self.health     = None
        self.isTouching = []
        
    def move(self, dx:int, dy:int) -> None:
        """ move the object """
        self.x += dx * (1 / DEFAULT_FPS )
        self.y += dy * (1 / DEFAULT_FPS )  
           
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.width)
        
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.height)
        
    def _kill(self) -> None:
        """ kill the object """
    
    def _takeDamage(self, damage:int) -> None:
        """ handle damage """
    
    def _draw(self) -> None:
        """ draw the object """
        if self.name.startswith('Floor'):
            if self.name == 'Floor_left':
                pyxel.blt(self.x, self.y, 1, 0, 0, self.width, self.height, 0)

            elif self.name == 'Floor_right':
                pyxel.blt(self.x, self.y, 1, 8, 0, self.width, self.height, 0)
        
            elif self.name == 'Floor_center':
                pyxel.blt(self.x, self.y, 1, 0, 8, self.width, self.height, 0)

    def _update(self) -> None:
        """ update the object """
        
        