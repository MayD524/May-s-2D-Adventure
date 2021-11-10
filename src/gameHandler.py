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
        for ent in self.gameObjects:
            ## TODO: check colision
            ## check if ent is touching player and if so, print the ent's name
            ## get the size of ent and player and check if they are touching
            ## if they are, print the ent's name
            if ent.x + ent.width > self.player.x and ent.x < self.player.x + self.player.width:
                if ent.y + ent.height > self.player.y and ent.y < self.player.y + self.player.height:
                    if ent.dmg > 0:
                        self.palyer.health -= ent.dmg
                        print(f"{ent.name} hit you for {ent.dmg} damage")
    
    def updateList(self, list:list) -> None:
        for elm in list:
            elm._update()
            
    def drawList(self, list:list) -> None:
        for elm in list:
            elm._draw()