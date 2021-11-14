from gameConsts import *
from gameEntity import mayGameEntity
import random
import pyxel
import time

class mayNPC(mayGameEntity):
    def __init__(self, x:int, y:int, w:int, h:int, hp:int, speed:int, name:str) -> None:
        super().__init__(x, y, w, h, 7, hp)
        self.direction = 1
        self.speed     = speed
        self.name      = name
        self.npc_type  = NPC_TYPE_ENEMY
        self.facing    = DIRECTION_FRONT
        self.canWait   = NPC_WAITING_ENABLED
        self.waitFor   = 0
    
    def _update(self) -> None:
        if self.isAlive:
            
            if self.waitFor > 0:
                self.facing = DIRECTION_FRONT
                self.waitFor -= 2 * (1 / DEFAULT_FPS)
                if self.waitFor <= 0:
                    self.waitFor = 0
                else:
                    return

            self.waitFor = random.randint(0, 10) if self.canWait else 0
                
            self.move((1 * self.speed) * self.direction, 0)
            
            shouldJump = random.random() if pyxel.frame_count % DEFAULT_FPS == 0 else 0
                
            if any(x for x in self.isTouching if x[1] == "left") or self.x == pyxel.width - self.width:
                self.direction = -1
                self.facing = DIRECTION_LEFT
                
            elif any(x for x in self.isTouching if x[1] == "right") or self.x == 0:
                self.direction = 1    
                self.facing = DIRECTION_RIGHT
                
            if shouldJump >= JUMP_CHANCE and not self.jump and not self.in_air:
                self._jump(DEFAULT_JUMP_HEIGHT)  
                self.facing = DIRECTION_FRONT
                    
            if self.yMove > 0:
                self.move(0, -1)
                self.yMove -= 1 if DEFAULT_FPS <= 30 else 1 / (DEFAULT_FPS / 30)
                if self.yMove <= 0:
                    self.jump = False

            if self.in_air and not self.jump:
                #self.facing = MAKE_BLOB_SMALL
                self.fall()
                
            if not self.in_air and not self.jump and self.waitFor > 2 and random.random() >= WAIT_CHANCE:
                print(self.waitFor)
                self.waitFor -= 2
            else:
                self.waitFor = 0
                
                            
    def _draw(self) -> None:
        if self.isAlive:
            if self.npc_type == NPC_TYPE_ENEMY:
                start_x = 16
                start_y = 0
                
                if self.facing == DIRECTION_LEFT:
                    start_y += 8
                elif self.facing == DIRECTION_RIGHT:
                    start_x += 8
                    
                pyxel.blt(self.x, self.y, 0, start_x, start_y, self.width, self.height, 0)
            #pyxel.rect(self.x, self.y, self.width, self.height, self.color)
            #pyxel.blt(self.x, self.y, 1, 0, 0, self.width, self.height, self.color)