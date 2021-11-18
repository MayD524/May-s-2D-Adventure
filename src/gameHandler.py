from concurrent.futures import ThreadPoolExecutor
from _thread import start_new_thread
from gameEntity  import mayGameEntity
from gameObjects import mayGameObject
from gameConsts import *
import pyxel

from npc import mayNPC

class GameHandler:
    def __init__(self):
        self.gameObjects:mayGameObject = []
        self.player:mayGameEntity = None
    
    def _cleanup(self) -> None:
        self.gameObjects:mayGameObject = [i for i in self.gameObjects if i.isAlive]
    
    def get_object(self, object_name:str) -> mayGameEntity:
        for obj in self.gameObjects:
            if obj.name == object_name:
                return obj
        return None
    
    def check_collision(self, agent:mayGameEntity) -> None:
        agent_box = (agent.x + agent.width, agent.y + agent.height)
        agentYRange = range(round(agent.y), round(agent_box[1]))
        agentXRange = range(round(agent.x), round(agent_box[0]))
        agent.isTouching = []
        onFloor = False
        
        if agent.name == "player":
            if agent.y >= 151:
                agent.health -= 100
                return
        
        for ent in self.gameObjects:
            ## ignore if it doesn't matter
            if (ent == agent or not ent.has_col):
                continue
            
            
            ent_box = (ent.x + ent.width, ent.y + ent.height)
            entXRange = range(round(ent.x), round(ent_box[0]))
            entYRange = range(round(ent.y), round(ent_box[1]))
            
            ## is touching an object
            if any(i in agentXRange for i in entXRange) and any(i in agentYRange for i in entYRange):
                touchingTup = (ent, )
                if ent.name == 'master_floor':
                    agent.isTouching.append((ent, 'top'))
                    agent.in_air = False
                    onFloor = True
                    continue

                ## check for bottom collision
                if agent.y > entYRange[0] and (agent.jump or agent.in_air):
                    touchingTup = (*touchingTup, 'bottom')
                    agent.y = entYRange[-1]
                    ## just so it doesn't hang there
                    if agent.jump:
                        agent.jump = False
                        agent.in_air = True
                        agent.yMove = 0
                        
                ## check for top collision
                elif agent_box[1] <= entYRange[0] + 1:
                    touchingTup = (*touchingTup, 'top')
                    onFloor = True
                    agent.in_air = False
                
                ## check for right collision
                elif agent.x > entXRange[0]:
                    touchingTup = (*touchingTup, 'right')
                    agent.x = entXRange[-1]
                        
                ## check for left collision
                elif agent_box[0] > entXRange[0]:
                    touchingTup = (*touchingTup, 'left')
                    agent.x = entXRange[0] - agent.width
                
                 
                if ent.dmg > 0 and agent.health:
                    agent._takeDamage(ent.dmg)
                
                agent.isTouching.append(touchingTup)
               
            ## set falling    
            else:
                agent.in_air = True if not onFloor else False
        
    def newObject(self, object_name:str, object_id:int, width:int, height:int) -> None:
        if object_id == GAME_ENTITY:
            ent = mayGameEntity(pyxel.width / 2, pyxel.height / 2, width, height, 5, 100)
            ent.name = object_name
            #self.entityList.append(ent)
            self.gameObjects.append(ent)

    
    def updateList(self, elmList:list[mayGameObject]) -> None:
        
        for elm in elmList:
            if elm.canMove or isinstance(elm, mayGameEntity):
                self.check_collision(elm)
                
            if elm.isAlive:
                ## do things that require gameHandler here
                if isinstance(elm, mayNPC) and elm.npc_type == NPC_RANGED_ENEMY and elm.shooting:
                    self.gameObjects.append(elm.spawn_projectile())
                    elm.shooting = False
        
        threads = [start_new_thread(elm._update, ()) for elm in elmList]  
        
            
            
    def drawList(self, list:list) -> None:
        for elm in list:
            if elm.isAlive:
                elm._draw()