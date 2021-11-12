from projectile import mayProjectile
from gameHandler import GameHandler
from gameConsts import *
from floor import mayFloor
from player import player
from npc import mayNPC
import pyxel
import math

class App(GameHandler):
    def __init__(self):
        GameHandler.__init__(self)
        pyxel.init(200, 160, caption="Pyxel Game")
        
        pyxel.load("my_resource.pyxres")
        
        self.scene = SCENE_PLAYING
        self.score = 0
        gameFloor = mayFloor(0, pyxel.height - 20, 200, 20)
        gameFloor.name = "master_floor"
        testFloor = mayFloor(10, pyxel.height - 55, 50, 10)
        testFloor.imgID = 1
        self.gameObjects.append(gameFloor)
        self.gameObjects.append(testFloor)
        #npc = mayNPC(30, pyxel.height - 50, 10, 10, 100, 1, "npc-1")
        #self.gameObjects.append(npc)
        
        self.player = player(pyxel.width / 2, pyxel.height - 40, TILEOFFSET + 1, TILEOFFSET + 1, p_health=100)
        pyxel.run(self.update, self.draw)
        
        
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btnp(pyxel.KEY_R):
            proj = mayProjectile(0, pyxel.height - 50, 10, 5, 6, 10, 1, 10)
            self.gameObjects.append(proj)
        
        if self.scene == SCENE_PLAYING:
            self.update_play()
            
    def draw(self) -> None:
        pyxel.cls(0)
    
        if self.scene == SCENE_PLAYING:
            self.draw_play_scene()
            
    def update_play(self) -> None:
        self.player._update()
        self.check_collision(self.player)
        self.updateList(self.gameObjects)
        self._cleanup()
        
    
    def draw_play_scene(self) -> None:
        self.player._draw()
        self.drawList(self.gameObjects)
        
            
        
if __name__ == "__main__":
    App()