import Window
import pygame

class NodePrototype:
    def __init__(self):
        # Window
        self.__window = Window.Window(800, 500, "Marinara Node Map Prototype")
        self.__running = True

    #=====[ THE BIG THREE ]==========
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitProgram()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.regenerateNodes()


    def updateProgram(self):
        ...
    
    def renderProgram(self):
        ...

    #=====[ KEYBOARD EVENTS ]=========
    def quitProgram(self):
        self.running = False
        pygame.quit()
    
    def regenerateNodes(self):
        ...

    #=====[ MAIN GAME LOOP ]==========
    def run(self):
        while self.__running:
            self.handleEvents()
            self.updateProgram()
            self.renderProgram()