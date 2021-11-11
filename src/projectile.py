from gameObjects import mayGameObject
import pyxel

class mayProjectile(mayGameObject):
    def __init__(self, x:int, y:int, width:int, height:int, color:int, speed:int, direction:int, damage:int):
        super().__init__(x, y, width, height, color, damage)
        self.color = color
        self.speed = speed
        self.direction = direction
        self.isAlive = True
        
    def _update(self):
        self.x += self.speed * self.direction
        if self.x > pyxel.width or self.x < 0:
            self.isAlive = False
            
    def _draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)