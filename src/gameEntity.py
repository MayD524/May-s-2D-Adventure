import pyxel

class mayGameEntity:
    def __init__(self, x:int, y:int, width:int, height:int, color:int, max_health:int):
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.color      = color
        self.health     = max_health
        
        self.is_alive = True
        self.in_air   = False
        
    def move(self, dx:int, dy:int) -> None:
        """ move the object """
        self.x += dx
        self.y += dy
        
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.width)
        
        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.height)
        
    def _takeDamage(self, damage:int):
        """ take damage from an attack """
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
    
    def _draw(self):
        """ draw a game entity (player, enemy, living) """
    
    def _update(self):
        """ update a game entity state (anything 'living') """
        