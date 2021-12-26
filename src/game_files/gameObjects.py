from game_files.gameConsts import *
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
        self.isInverted = False
        self.centerPoint= (self.x + self.width // 2, self.y + self.height // 2)
        
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
            x = 0
            y = 0

            if 'Floor_right' in self.name:
                x += 8
        
            elif 'Floor_center' in self.name:
                y += 8
                
            if self.isInverted:
                x += 16
                
            pyxel.blt(self.x, self.y, 1, x, y, self.width, self.height, 0)

    def _update(self) -> None:
        """ update the object """
        
        