from projectile import mayProjectile
from gameHandler import GameHandler
from collectables import *
from gameConsts import *
from floor import mayFloor
from player import player
from npc import mayNPC
import pyxel
import math

class App(GameHandler):
    def __init__(self):
        GameHandler.__init__(self)
        pyxel.init(208, 160, caption="Pyxel Game", fps=DEFAULT_FPS)
        pyxel.load("my_resource.pyxres")
        self.game_Init()
        pyxel.run(self.update, self.draw)
        
    ## made a separate function so that we can call it later
    def game_Init(self) -> None:
        self.gameObjects = []
        self.scene      = SCENE_PLAYING
        self.score      = 0
        self.pHealth    = PLAYER_DEFAULT_HEALTH
        gameFloor       = mayFloor(0, pyxel.height - 20, 208, 20)
        gameFloor.name  = "master_floor"
        
        testFloor = mayFloor(10, pyxel.height - 28, 48, 8)
        test2Floor = mayFloor(60, pyxel.height - 50, 48, 8)
        test3Floor = mayFloor(110, 30, 16, 8)
        self.gameObjects.append(mayCoin(60, 120))
        self.gameObjects.append(mayHealthKit(80, 120))
        
        test2Floor.imgID = 1
        test2Floor.name = "test2_floor"
        
        testFloor.name = "test_floor"
        testFloor.imgID = 1
        
        self.gameObjects.append(gameFloor)
        self.gameObjects.append(testFloor)
        self.gameObjects.append(test2Floor)
        self.gameObjects.append(test3Floor)
        
        #npc = mayNPC(30, pyxel.height - 50, 8, 8, 100, .4, NPC_SIMPLE_ENEMY ,"enemy-npc-1")
        #self.gameObjects.append(npc)
        
        npc = mayNPC(60, pyxel.height - 50, 8, 8, 100, .4, NPC_RANGED_ENEMY ,"enemy-npc-1")
        self.gameObjects.append(npc)
        
        self.player = player(pyxel.width / 2, pyxel.height - 40, TILEOFFSET + 1, TILEOFFSET + 1, p_health=self.pHealth)
        
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btnp(pyxel.KEY_R):
            proj = mayProjectile(0, pyxel.height - 50, 10, 5, 6, 10, 1, 10)
            self.gameObjects.append(proj)
        
        if self.scene == SCENE_PLAYING:
            self.update_play()
            
        elif self.scene == SCENE_END:
            self.update_gameOver()
            
    def draw(self) -> None:
        pyxel.cls(0)
    
        if self.scene == SCENE_PLAYING:
            self.draw_play_scene()
            
        elif self.scene == SCENE_END:
            self.draw_game_over()
            
    def update_gameOver(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.game_Init()
    
    def update_play(self) -> None:
        self.player._update()
        self.score = self.player.score
        self.pHealth = self.player.health
        
        if self.pHealth <= 0:
            self.scene = SCENE_END
            
        self.check_collision(self.player)
        self.updateList(self.gameObjects)
        self._cleanup()
        
    def draw_game_over(self) -> None:
        pyxel.text(pyxel.width / 2, pyxel.height / 2, "GAME OVER", 7)
        pyxel.text(pyxel.width / 2, (pyxel.height / 2) + 8, f"Score: {self.score}", 6)    
    
    def draw_play_scene(self) -> None:
        self.player._draw()
        pyxel.text(0, 0, f"Score: {self.score}", 6)
        pyxel.text(0, 8, f"Health: {self.pHealth}", 6)
        self.drawList(self.gameObjects)    
        
if __name__ == "__main__":
    App()