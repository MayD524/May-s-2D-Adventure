import pygame

BACKGROUND_COLOR = (0, 0, 0)
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
            return True
                    
        self.draw(screen)
    
    def draw(self, screen:pygame.Surface) -> None:
        
        if self.isFull:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.default_color, (self.x, self.y, self.width, self.height), 2)

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
        
        self.init_draw()
        
    
    def init_draw(self):
        '''
            Just draw the basic buttons and stuff
        '''
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(GAME_WIDTH - 64, 0, 64, GAME_HEIGHT), 2)    
        self.buttons = [
            mapMaker_button(GAME_WIDTH - 64, 0, 64, 64, (255, 0, 1), 1),
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
                    
                

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    app = MapMaker(screen)
    app.gameMain()
    pygame.quit()