from gameEntity import mayGameEntity
import pyxel
import random

class mayNPC(mayGameEntity):
    def __init__(self, x:int, y:int, w:int, h:int, hp:int, speed:int, name:str) -> None:
        super().__init__(x, y, w, h, 7, hp)
        self.speed = speed 
        self.name = name
        
    def _update(self) -> None:
        if self.isAlive:
            move = random.random() * random.randint(-1, 1)
            times = random.randint(1, 20)
            for i in range(times):
                self.move(move, 0)
            
            if self.in_air and not self.jump:
                self.fall()
            
    def _draw(self) -> None:
        if self.isAlive:
            pyxel.rect(self.x, self.y, self.width, self.height, self.color)