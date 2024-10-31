import pygame
import NodeMap.Node as NODE

class NodeMap:
    def __init__(self, node_surface, connection_surface):
        self.__node_map = getBlankNodeMap()
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
    
    def drawConnection(self, points):
        connection = [0, 0, 0, 0]

        if type(points[0]) is NODE.Node:
            connection[0] = points[0].getX()
            connection[1] = points[0].getY()
            connection[2] = points[1].getX()
            connection[3] = points[1].getY()
        
        else:
            for i in range(len(points)):
                connection[i] = points[i]
        
        #if [connection[0], connection[3], connection[2], connection[1]] not in self.__connections:
        if self.connectionValid(connection):
            self.__connections.append(connection)
            pygame.draw.line(self.__connection_surface, (0, 0, 0),
                (connection[0]*100+50, connection[1]*100+50),
                (connection[2]*100+50, connection[3]*100+50), 3
            )
                

    #=====[ GETTERS ]==========
    def getCell(self, x, y):
        return self.__node_map[y][x]
    
    def containsConnection(self, connection_):
        connection = [connection_[0], connection_[1], connection_[2], connection_[3]]
        if connection in self.__connections:
            return True
        return False

    def connectionValid(self, connection):
        if type(connection[0]) is NODE.Node:
            p1 = (connection[0].getPos())
            p2 = (connection[1].getPos())
        else:
            p1 = (connection[0], connection[1])
            p2 = (connection[2], connection[3])
        
        temp_connection  = [p1[0], p1[1], p2[0], p2[1]]
        cross_connection = [p1[0], p2[1], p2[0], p1[1]]

        if self.containsConnection(temp_connection):
            return False
        if self.containsConnection(cross_connection):
            return False

        return True


    def isConnectedTo(self, node):
        if type(node) is NODE.Node:
            x,y = node.getPos()
        else:
            x, y = node
        
        for connection in self.__connections:
            if connection[2] == x and connection[3] == y:
                return True
        
        return False
    
        
    def hasConnectionFrom(self, node):
        if type(node) is NODE.Node:
            x,y = node.getPos()
        else:
            x, y = node
        
        for connection in self.__connections:
            if connection[0] == x and connection[1] == y:
                return True
        
        return False
    

    #=====[ SETTERS ]==========
    def setCell(self, node):
        self.setCell(node.getPos()[0], node.getPos()[1], node)
        self.drawNode(node)
    
    def setCell(self, x: int, y: int, type: str):
        new_node = NODE.Node().at(x, y).ofType(type).isReal()
        self.__node_map[y][x] = new_node
        self.drawNode(new_node)
    
    def reset(self):
        self.__node_map = getBlankNodeMap()
        self.__connections = []
        self.__node_surface      .fill((0, 0, 0, 0))
        self.__connection_surface.fill((0, 0, 0, 0))
    
    #def addConnection(self, x1, y1, x2, y2):
    #    self.__connections.append((x1, y1, x2, y2))
    #    self.drawConnection((x1, y1, x2, y2))

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        string = ""

        for row in self.__node_map:
            for x in row:
                string = string + (x.__str__() + " ").ljust(15, " ")
            string = string + "\n"

        return string



def getBlankNodeMap():
    nodemap = []

    for y in range(5):
        temp_row = []
        for x in range(8):
            temp_row.append(NODE.Node().at(x, y))
        nodemap.append(temp_row)
    
    return nodemap