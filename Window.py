import pygame

class Window:
    def __init__(self, width, height, name):
        # Window Settings
        self.__WINDOW_WIDTH  = width
        self.__WINDOW_HEIGHT = height
        self.__WINDOW_NAME   = name

        # Defining the Window
        pygame.init()
        self.window = pygame.display.set_mode((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT))
        pygame.display.set_caption(self.__WINDOW_NAME)

        # Extra Surfaces
        self.__background_surface =                                     \
            pygame.Surface((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT))

        self.__grid_surface       =                                     \
            pygame.Surface((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT)) \
            .convert_alpha()
        self.__node_surface       =                                     \
            pygame.Surface((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT)) \
            .convert_alpha()
        self.__connection_surface =                                     \
            pygame.Surface((self.__WINDOW_WIDTH, self.__WINDOW_HEIGHT)) \
            .convert_alpha()

        self.wipeScreen()
    
    #=====[ MUTATORS ]==========
    def render(self):
        self.window.blit(self.__background_surface, (0, 0))
        self.window.blit(self.__grid_surface, (0, 0))
        self.window.blit(self.__node_surface, (0, 0))
        self.window.blit(self.__connection_surface, (0, 0))
        pygame.display.flip()
    
    
    def wipeScreen(self):
        self.__background_surface.fill((200, 200, 200))
        self.__grid_surface      .fill((0, 0, 0, 0))
        self.__node_surface      .fill((0, 0, 0, 0))
        self.__connection_surface.fill((0, 0, 0, 0))

        self.drawGrid()
    

    def drawGrid(self):
        # Drawing vertical lines first
        for x in range(1,self.__WINDOW_WIDTH // 100 + 1):
            pygame.draw.line(self.__grid_surface, (0, 0, 0),
                             (x*100, 0), (x*100, self.__WINDOW_HEIGHT))
        
        # Then hortizontal lines
        for y in range(1,self.__WINDOW_HEIGHT // 100 + 1):
            pygame.draw.line(self.__grid_surface, (0, 0, 0),
                             (0, y*100), (self.__WINDOW_WIDTH, y*100))
        
    
    #=====[ GETTERS ]==========
    def getGridSurface(self):
        return self.__grid_surface
    
    def getNodeSurface(self):
        return self.__node_surface
    
    def getConnectionSurface(self):
        return self.__connection_surface
    

    #=====[ SETTERS ]==========
    
    

    #=====[ DUNDER ZONE ]==========