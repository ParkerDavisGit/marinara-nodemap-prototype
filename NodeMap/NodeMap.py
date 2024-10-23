class NodeMap:
    def __init__(self):
        self.__node_map = [["x" for x in range(8)] for y in range(5)]

    #=====[ GETTERS ]==========
    def getCell(self, x, y):
        return self.__node_map[y][x]

    #=====[ SETTERS ]==========
    def setCell(self, node):
        self.setCell(node.getPos()[0], node.getPos()[1], node.getType())
    
    def setCell(self, x: int, y: int, type: str):
        self.__node_map[y][x] = type
    
    def reset(self):
        self.__node_map = [["x " for x in range(8)] for y in range(5)]

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        string = ""

        for row in self.__node_map:
            for x in row:
                string = string + (x + " ").ljust(15, " ")
            string = string + "\n"

        return string