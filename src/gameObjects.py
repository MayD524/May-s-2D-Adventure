import pyxel
import math

class mayGameObject:
    def __init__(self, x:int, y:int, w:int, h:int, has_col:bool, damageOnCol:int) -> None:
        self.x       = x
        self.y       = y
        self.width   = w
        self.height  = h
        self.has_col = has_col
        self.dmg     = damageOnCol
        self.isAlive = True
        self.canMove = False
        self.name    = "mayGameObject"
        self.health  = None
        
    def move(self, dx:int, dy:int) -> None:
        """ move the object """
        self.x += dx
        self.y += dy
        
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
        
    def _update(self) -> None:
        """ update the object """
        
        