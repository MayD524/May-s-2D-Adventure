from gameEntity  import mayGameEntity
from gameObjects import mayGameObject
import pyxel


class GameHandler:
    def __init__(self):
        self.entityList:mayGameEntity = []
        self.gameObjects:mayGameObject = []
        self.player:mayGameEntity = None
    
    def _cleanup(self) -> None:
        self.entityList:mayGameEntity = [i for i in self.entityList if i.isAlive]
        self.gameObjects:mayGameObject = [i for i in self.gameObjects if i.isAlive]
    
    def check_colision(self) -> None:
        player_box = (self.player.x + self.player.width, self.player.y + self.player.height)
        playerXRange = range(round(self.player.x), round(player_box[0]))
        playerYRange = range(round(self.player.y), round(player_box[1]))
        
        for ent in self.gameObjects:
            ent_box = (ent.x + ent.width, ent.y + ent.height)
            entXRange = range(round(ent.x), round(ent_box[0]))
            entYRange = range(round(ent.y), round(ent_box[1]))
            
            if any(i in playerXRange for i in entXRange) and any(i in playerYRange for i in entYRange):
                if ent.name == 'floor':
                    self.player.in_air = False
                    
            else:
                if ent.name == 'floor':
                    self.player.in_air = True
            
        
                        
    def updateList(self, list:list) -> None:
        for elm in list:
            elm._update()
            
    def drawList(self, list:list) -> None:
        for elm in list:
            elm._draw()