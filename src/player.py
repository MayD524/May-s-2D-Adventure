from gameConsts import *
from gameEntity import mayGameEntity
import pyxel

from gameObjects import mayGameObject

class player(mayGameEntity):
    def __init__(self, x:int, y:int, w:int, h:int, p_health:int) -> None:
        mayGameEntity.__init__(self, x, y, w, h, None, p_health)
        self.name      = 'player'
        self.score     = 0
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
            self._jump(DEFAULT_JUMP_HEIGHT)
        
        if pyxel.btn(pyxel.KEY_DOWN):
            self.direction = MAKE_BLOB_SMALL
            if self.jump and self.yMove < DEFAULT_JUMP_HEIGHT / 2:
                self.jump = False
                self.in_air = True
                self.yMove = 0
                self.fallRate += -3
                
        else:
            self.fallRate = DEFAULT_FALL_RATE
        
        for (blob, direction) in self.isTouching:
            if not blob.isAlive:
                continue
            
            if blob.name == 'coin':
                self.score += blob.incScore
                blob.isAlive = False
                
            if isinstance(blob, mayGameEntity):
                if blob.npc_type in NPC_TYPE_ENEMY and direction == 'top':
                    blob.isAlive = False
                    self.score += 1
                    
                elif blob.npc_type in NPC_TYPE_ENEMY and direction != "top":
                    self.health -= 10
                    
            elif isinstance(blob, mayGameObject):
                if blob.name == 'healthKit':
                    self.health += blob.health_inc
                    if self.health > PLAYER_DEFAULT_MAX_HEALTH:
                        self.health = PLAYER_DEFAULT_MAX_HEALTH
                    blob.isAlive = False
                    
        if self.in_air and not self.jump:
            self.fall()
        
        ## handle jumping
        elif self.yMove != 0:
            self.move(0, self.fallRate)
            self.yMove -= 1 if DEFAULT_FPS <= 30 else 1 / (DEFAULT_FPS / 30)
            if self.yMove == 0:
                self.jump = False
        ## handle actions
        
    def _draw(self):
        tileXOffSet = 0
        tileYOffSet = 0
        if self.direction == DIRECTION_LEFT or self.direction == MAKE_BLOB_SMALL:
            #tileXOffSet = TILEOFFSET
            tileYOffSet = TILEOFFSET
        
        if self.direction == DIRECTION_RIGHT or self.direction == MAKE_BLOB_SMALL:
            tileXOffSet = TILEOFFSET    

        pyxel.blt(self.x, self.y, 0, tileXOffSet, tileYOffSet, TILEOFFSET, TILEOFFSET, 2)
        #pyxel.rect(self.x, self.y, self.width, self.height, 7)