import pygame
import NodeMap.Node as NODE

class NodeMap:
    def __init__(self, node_surface, connection_surface):
        self.__node_map = [["x" for x in range(8)] for y in range(5)]
        self.__connections        = []

        self.__node_surface       = node_surface
        self.__connection_surface = connection_surface

    #=====[ MUTATORS ]==========
    def render(self):
        for row in self.__node_map:
            for node in row:
                self.drawNode(node)
    
    def drawNode(self, node):
        if type(node) is not NODE.Node:
            return
        if node.getType() == "SHOP":
            pygame.draw.circle(
                self.__node_surface, (55, 55, 215), 
                (node.getX()*100+50, node.getY()*100+50),
                30
            )
        elif node.getType() == "WAVEDEFENSE":
            pygame.draw.circle(
                self.__node_surface, (215, 55, 55), 
                (node.getX()*100+50, node.getY()*100+50),
                30
            )
        elif node.getType() == "EXPLORATION":
            pygame.draw.circle(
                self.__node_surface, (55, 215, 55), 
                (node.getX()*100+50, node.getY()*100+50),
                30
            )
        elif node.getType() == "TREASURE":
            pygame.draw.circle(
                self.__node_surface, (255, 215, 0), 
                (node.getX()*100+50, node.getY()*100+50),
                30
            )
        elif node.getType() == "BOSS":
            pygame.draw.circle(
                self.__node_surface, (55, 55, 55), 
                (node.getX()*100+50, node.getY()*100+50),
                30
            )
    
    def drawConnection(self, connection):
        pygame.draw.line(self.__node_surface, (0, 0, 0),
            (connection[0]*100+50, connection[1]*100+50),
            (connection[2]*100+50, connection[3]*100+50), 3
        )
                

    #=====[ GETTERS ]==========
    def getCell(self, x, y):
        return self.__node_map[y][x]

    #=====[ SETTERS ]==========
    def setCell(self, node):
        self.setCell(node.getPos()[0], node.getPos()[1], node)
        self.drawNode(node)
    
    def setCell(self, x: int, y: int, type: str):
        new_node = NODE.Node().at(x, y).ofType(type)
        self.__node_map[y][x] = new_node
        self.drawNode(new_node)
    
    def reset(self):
        self.__node_map = [["x " for x in range(8)] for y in range(5)]
    
    def addConnection(self, x1, y1, x2, y2):
        self.__connections.append((x1, y1, x2, y2))
        self.drawConnection((x1, y1, x2, y2))

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        string = ""

        for row in self.__node_map:
            for x in row:
                string = string + (x.__str__() + " ").ljust(15, " ")
            string = string + "\n"

        return string