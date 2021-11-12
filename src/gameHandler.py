from gameEntity  import mayGameEntity
from gameObjects import mayGameObject
import pyxel

GAME_ENTITY = 0
GAME_OBJECT = 1

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
        
        onFloor = False
        
        for ent in self.gameObjects:
            if (ent == agent or not ent.has_col):
                continue
            
            ent_box = (ent.x + ent.width, ent.y + ent.height)
            entXRange = range(round(ent.x), round(ent_box[0]))
            entYRange = range(round(ent.y), round(ent_box[1]))
            
            ## is touching an object
            if any(i in agentXRange for i in entXRange) and any(i in agentYRange for i in entYRange):
                if ent.name == 'master_floor':
                    agent.in_air = False
                    onFloor = True
                    continue

                ## check for botoom collision
                if agent.y > entYRange[0]:
                    agent.y = entYRange[-1]
                    
                ## check for top collision
                elif agent_box[1] <= entYRange[0] + 1:
                    onFloor = True
                    self.player.in_air = False
                
                ## check for right collision
                elif agent.x > entXRange[0]:
                    agent.x = entXRange[-1]
                        
                ## check for left collision
                elif agent_box[0] > entXRange[0]:
                    agent.x = entXRange[0] - agent.width
                
                 
                if ent.dmg > 0 and agent.health:
                    agent._takeDamage(ent.dmg)
                    print(agent.health)
                        
            
            ## set falling    
            else:
                agent.in_air = True if not onFloor else False
    
    def newObject(self, object_name:str, object_id:int, width:int, height:int) -> None:
        if object_id == GAME_ENTITY:
            ent = mayGameEntity(pyxel.width / 2, pyxel.height / 2, width, height, 5, 100)
            ent.name = object_name
            #self.entityList.append(ent)
            self.gameObjects.append(ent)
              
    def updateList(self, list:list) -> None:
        for elm in list:

            if elm.canMove:
                self.check_collision(elm)
            elm._update()
            
            
    def drawList(self, list:list) -> None:
        for elm in list:
            elm._draw()