from game_files.gameConsts import *
import pyxel

class mayGameEntity:
    def __init__(self, x:int, y:int, width:int, height:int, color:int, max_health:int):
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.color      = color
        self.health     = max_health
        self.speed      = DEFAULT_SPEED
        self.yMove      = 0
        self.dmg        = 0 ## change if you want to have different damage values
        self.fallRate   = DEFAULT_FALL_RATE
        
        self.isTouching = []
        
        self.isAlive  = True
        self.has_col  = True
        self.in_air   = True
        self.jump     = False
        self.canMove  = True
        self.name     = None
        self.centerPoint = (self.x + self.width // 2, self.y + self.height // 2)
        
    def move(self, dx:int, dy:int) -> None:
        """ move the object """
        speedCap = 1
        if DEFAULT_FPS > 30:
            speedCap = 1 / (DEFAULT_FPS / 30)
        
            
        self.x += dx * speedCap
        self.y += dy * speedCap
        
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.width)
        
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.height)
        
    def fall(self) -> None:
        """ Make entity fall """
        if self.in_air:
            self.move(0, 1)
    
    def _jump(self, end_height:int) -> None:
        """ jump to a height """
        self.jump   = True
        self.yMove  = end_height
    
    def _takeDamage(self, damage:int):
        """ take damage from an attack """
        self.health -= damage
        if self.health <= 0:
            self.isAlive = False
            print("You died!")
    
    def _draw(self):
        """ draw a game entity (player, enemy, living) """
        if self.isAlive:
            pyxel.rect(self.x, self.y, self.width, self.height, self.color)
    
    def _update(self):
        """ update a game entity state (anything 'living') """
        if self.in_air and not self.jump:
            self.fall()        