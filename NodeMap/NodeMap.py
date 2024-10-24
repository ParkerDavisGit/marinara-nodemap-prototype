import pygame
import NodeMap.Node as NODE

class NodeMap:
    def __init__(self, node_surface, connection_surface):
        self.__node_map = [["x" for x in range(8)] for y in range(5)]
        self.__node_surface       = node_surface
        self.__connection_surface = connection_surface

    #=====[ MUTATORS ]==========
    def render(self):
        for row in self.__node_map:
            for node in row:
                if type(node) is not NODE.Node:
                    continue
                if node.getType() == "TREASURE":
                    pygame.draw.circle(
                        self.__node_surface, (255, 215, 0), 
                        (node.getX()*100+50, node.getY()*100+50),
                        30
                    )
                elif node.getType() == "TREASURE":
                    pygame.draw.circle(
                        self.__node_surface, (255, 215, 0), 
                        (node.getX()*100+50, node.getY()*100+50),
                        30
                    )

    #=====[ GETTERS ]==========
    def getCell(self, x, y):
        return self.__node_map[y][x]

    #=====[ SETTERS ]==========
    def setCell(self, node):
        self.setCell(node.getPos()[0], node.getPos()[1], node)
    
    def setCell(self, x: int, y: int, type: str):
        self.__node_map[y][x] = NODE.Node().at(x, y).ofType(type)
    
    def reset(self):
        self.__node_map = [["x " for x in range(8)] for y in range(5)]

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        string = ""

        for row in self.__node_map:
            for x in row:
                string = string + (x.__str__() + " ").ljust(15, " ")
            string = string + "\n"

        return string