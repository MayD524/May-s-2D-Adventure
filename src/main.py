from gameEntity import mayGameEntity
from gameHandler import GameHandler
from gameObjects import mayGameObject
from floor import mayFloor
from player import player
import pyxel
import math

SCENE_TITLE   = 0
SCENE_PLAYING = 1
SCENE_END     = 2
SCENE_WIN     = 3


class App(GameHandler):
    def __init__(self):
        GameHandler.__init__(self)
        pyxel.init(200, 160, caption="Pyxel Game")
        
        pyxel.image(0).set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b07c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0",
            ],
        )

        pyxel.image(0).set(
            8,
            0,
            [
                "00088000",
                "00ee1200",
                "08e2b180",
                "02882820",
                "00222200",
                "00012280",
                "08208008",
                "80008000",
            ],
        )
        
        self.scene = SCENE_PLAYING
        self.score = 0
        self.player = player(pyxel.width / 2, pyxel.height - 40, 10, 10, p_health=100)
        gameFloor = mayFloor(0, pyxel.height - 20, 200, 20)
        testFloor = mayFloor(10, pyxel.height - 30, 50, 10)
        self.gameObjects.append(gameFloor)
        self.gameObjects.append(testFloor)
        
        pyxel.run(self.update, self.draw)
        
        
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
            
        if self.scene == SCENE_PLAYING:
            self.update_play()
            
    def draw(self) -> None:
        pyxel.cls(0)
    
        if self.scene == SCENE_PLAYING:
            self.draw_play_scene()
            
    def update_play(self) -> None:
        self.player._update()
        self.updateList(self.entityList)
        self.updateList(self.gameObjects)
        self.check_colision()
        
    def draw_play_scene(self) -> None:
        self.player._draw()
        self.drawList(self.entityList)
        self.drawList(self.gameObjects)
            
        
if __name__ == "__main__":
    App()