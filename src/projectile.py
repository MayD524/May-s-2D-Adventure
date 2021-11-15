from gameObjects import mayGameObject
import pyxel

class mayProjectile(mayGameObject):
    def __init__(self, x:int, y:int, width:int, height:int, color:int=1, speed:int=1, direction:int=1, damage:int=10):
        super().__init__(x, y, width, height, color, damage)
        self.color = color
        self.speed = speed
        self.direction = direction
        self.isAlive = True
        self.canMove = True
        self.jump = False
        self.in_air = False
        self.name = "Projectile"
        
    def _update(self):
        self.x += self.speed * self.direction
        if self.x > pyxel.width or self.x < 0:
            self.isAlive = False
            
        if len(self.isTouching) > 0:
            self.isAlive = False
            
    def _draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)