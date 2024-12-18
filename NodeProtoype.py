import Window
import NodeMap.NodeMap as NODEMAP
import NodeMap.NodeMapRandomizer as NMRANDOM

import pygame

class NodePrototype:
    def __init__(self):
        # Window
        self.__window  = Window.Window(800, 500, "Marinara Node Map Prototype")
        self.__nodes   = NODEMAP.NodeMap(
            self.__window.getNodeSurface(), self.__window.getConnectionSurface())
        self.__running = True

    #=====[ THE BIG THREE ]==========
    def testFunc(self):
        print("Activating Test Mode")
        print("")
        
        print("")
        print("Deactivating Test Mode")

    #=====[ THE BIG THREE ]==========
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitProgram()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.regenerateNodes()
                    #self.testFunc()
                
                if event.key == pygame.K_ESCAPE:
                    self.quitProgram()


    def updateProgram(self):
        ...
    
    def renderProgram(self):
        self.__window.render()

    #=====[ KEYBOARD EVENTS ]=========
    def quitProgram(self):
        self.__running = False
    
    def regenerateNodes(self):
        NMRANDOM.randomizeNodeMap(self.__nodes)

    #=====[ MAIN GAME LOOP ]==========
    def run(self):
        while self.__running:
            self.handleEvents()
            self.updateProgram()
            self.renderProgram()
        
        pygame.quit()