import argparse
import pygame


BACKGROUND_COLOR = (0, 0, 0)

DEFAULT_CELL_COLOR = (255, 0, 255)


## Floor types 
MASTER_FLOOR = (20, 64, 13)
FLOOR_TYPE_GRASS = (34, 130, 18)
FLOOR_TYPE_ANIT  = (143, 17, 166)

## Player
PLAYER_SPAWN = (240, 250, 47)

## NPC
NPC_TYPE1_SPAWN = (201, 26, 50) ## default
NPC_TYPE2_SPAWN = (85, 38, 201) ## ranged

## Collectables
COIN_SPAWN = (154, 204, 27)
HEALTH_SPAWN = (148, 224, 213)


GAME_WIDTH = 1728
GAME_HEIGHT = 1280

class mapMaker_box:
    def __init__(self, x:int, y:int, width:int, height:int, color:tuple[int], numerical_value:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.default_color = color
        self.color = color
        self.numerical_value = numerical_value
        self.isFull = False
        
        self.hitBox = (range(self.x, self.x + self.width), range(self.y, self.y + self.height))
    
    def getState(self) -> tuple:
        return (self.isFull, self.color, self.x, self.y)
    
    def setState(self, new_color:tuple) -> None:
        self.color = new_color
    
    def check_if_clicked(self, mouse_pos:tuple[int], screen:pygame.Surface) -> bool:
        if mouse_pos[0] in self.hitBox[0] and mouse_pos[1] in self.hitBox[1]:
            self.isFull = not self.isFull
            if not self.isFull:
                self.color = self.default_color
            return True
                    
        self.draw(screen)
    
    def draw(self, screen:pygame.Surface) -> None:
        
        if self.isFull:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)

class mapMaker_button:
    def __init__(self, x:int, y:int, width:int, height:int, color:tuple[int], numerical_value:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.numerical_value = numerical_value
    
        self.hitBox = (range(self.x, self.x + self.width), range(self.y, self.y + self.height))
    
    def getState(self) -> tuple:
        return self.color
    
    def isClicked(self, mouse_pos:tuple[int]) -> bool:
        if mouse_pos[0] in self.hitBox[0] and mouse_pos[1] in self.hitBox[1]:
            return True
        return False
   
    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
   
class MapMaker:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.game = [[0 for x in range(GAME_WIDTH)] for y in range(GAME_HEIGHT)]
        self.running = True
        
        self.cells:mapMaker_box = []
        self.cureMode:tuple[int] = (255, 0, 255)
        self.isPressed = []
        
        self.mouseDown = False
        self.prevClicked = []
        
        parser = argparse.ArgumentParser()
        parser.add_argument("-m", "--map_name", type=str, default="map.mtdmap")

        self.args = parser.parse_args()
        
        self.init_draw()
        
    
    def init_draw(self):
        '''
            Just draw the basic buttons and stuff
        '''
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(GAME_WIDTH - 64, 0, 64, GAME_HEIGHT), 2)    
        self.buttons = [
            mapMaker_button(GAME_WIDTH - 64, 0, 64, 64, MASTER_FLOOR, 1),
            mapMaker_button(GAME_WIDTH - 64, 64, 64, 64, FLOOR_TYPE_GRASS, 2),
            mapMaker_button(GAME_WIDTH - 64, 128, 64, 64, FLOOR_TYPE_ANIT, 3),
            mapMaker_button(GAME_WIDTH - 64, 192, 64, 64, PLAYER_SPAWN, 4),
            mapMaker_button(GAME_WIDTH - 64, 256, 64, 64, NPC_TYPE1_SPAWN, 5),
            mapMaker_button(GAME_WIDTH - 64, 320, 64, 64, NPC_TYPE2_SPAWN, 6),
            mapMaker_button(GAME_WIDTH - 64, 384, 64, 64, COIN_SPAWN, 7),
            mapMaker_button(GAME_WIDTH - 64, 448, 64, 64, HEALTH_SPAWN, 8),
        ]
        for y in range(0, GAME_HEIGHT, 64):
            for x in range(0, GAME_WIDTH - 120, 64):
                #pygame.draw.rect(self.screen, (255, 0, 255), pygame.Rect(x, y, 64, 64), 2)
                self.cells.append(mapMaker_box(x, y, 64, 64, (255, 0, 255), y+x))
                
        self.draw_hud()
        self.draw_grid()
        pygame.display.update()

    def draw_hud(self) -> None:
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(GAME_WIDTH - 64, 0, 64, GAME_HEIGHT), 2)    

        for btn in self.buttons:
            btn.draw(self.screen)
    
    def draw_grid(self) -> None:
        for cell in self.cells:
            cell.draw(self.screen)

    
    def draw_screen(self):
        self.screen.fill(BACKGROUND_COLOR)
        #pygame.display.flip()
        self.draw_grid()
        self.draw_hud()
        pygame.display.update()   
         
    def draw_at_cursor(self) -> None:
        
        for btn in self.buttons:
            if btn.isClicked(pygame.mouse.get_pos()):
                self.cureMode = btn.getState()
        
        for cell in self.cells:
            if cell in self.prevClicked:
                continue
            
            isClicked = cell.check_if_clicked(pygame.mouse.get_pos(), self.screen)
            if isClicked:
                cell.setState(self.cureMode)
                cell.draw(self.screen)        
                self.prevClicked.append(cell)

        self.draw_screen()
    
    def save_map(self) -> None:
        ## save the map
        with open(self.args.map_name, 'wb') as f:
            for cell in self.cells:
                cell_state = cell.getState()
                f.write(bytes([cell_state[1][0] if cell_state[1][0] != 255 and cell_state[0] else 0]))
                
                
    
    def check_hotkeys(self) -> None:
        if pygame.K_LCTRL in self.isPressed:
            if pygame.K_s in self.isPressed:
                self.save_map()
    
    def gameMain(self):
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                
                if event.type == pygame.KEYUP and event.key in self.isPressed:
                    self.isPressed.remove(event.key)
                
                if event.type == pygame.KEYDOWN:
                    self.isPressed.append(event.key)
                    
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouseDown = False
                    self.prevClicked = []
                    
                if event.type == pygame.MOUSEBUTTONDOWN or self.mouseDown:
                    self.draw_at_cursor()
                    self.mouseDown = True
                    
            self.check_hotkeys()
                    
                

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    app = MapMaker(screen)
    app.gameMain()
    pygame.quit()