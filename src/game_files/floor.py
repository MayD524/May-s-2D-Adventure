from game_files.gameObjects import mayGameObject
import pyxel

class mayFloor:
    def __init__(self, x, y, width:int=200, height:int=50, inverted:bool=False):
        
        if width % 8 != 0:
            print("Floor width must be a multiple of 8, this may cause issues with drawing.")
        
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height
        self.has_col    = True
        self.dmg        = 0
        self.isAlive    = True
        self.canMove    = False
        self.name       = "Floor"
        self.health     = None
        self.isTouching = []
        self.isInverted = inverted
        
        leftEnd = mayGameObject(x, y, 8, 8, True, 0)
        rightEnd = mayGameObject(x+width-8, y, 8, 8, True, 0)
        
        leftEnd.name = "Floor_left"
        rightEnd.name = "Floor_right"
        leftEnd.isInverted = self.isInverted
        rightEnd.isInverted = self.isInverted
        
        self.blobs = [leftEnd, rightEnd]
        if width > 16:
            midStart = x + 8
            midEnd = x + width - 16
            midSection = []
            for tx in range(midStart, midEnd, 16):
                midSection.append(mayGameObject(tx, y, 16, 8, True, 0))
            
            for mid in midSection: mid.name = "Floor_center"; mid.isInverted = self.isInverted
            self.blobs.extend(midSection)
        if width - 16 == 8:
            mid = mayGameObject(x + 8, y, 8, 8, True, 0)
            mid.name = "Floor_center"; mid.isInverted = self.isInverted
            self.blobs.append(mid)
        ## blobs are each section of the floor
        self.name = "floor"
        self.imgID = None
        
    def _update(self):
        pass
    
    def _draw(self):
        for blob in self.blobs:
            blob._draw()
        #pyxel.blt(self.x, self.y, self.imgID, 0, 0, self.width, self.height)