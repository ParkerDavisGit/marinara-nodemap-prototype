class Node:
    def __init__(self):
        self.__x    = 0
        self.__y    = 0
        self.__type = ""
    
    #=====[ GETTERS ]==========
    def getPos(self):
        return (self.__x, self.__y)
    
    def getType(self):
        return self.__type

    #=====[ SETTERS ]==========
    def at(self, x, y):
        self.__x = x
        self.__y = y
    
    def ofType(self, new_type):
        self.__type = new_type

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        return f"{self.__type} - ({self.__x}, {self.__y})"
    
    def __deepcopy__(self):
        return Node().at(self.__x, self.__y).ofType(self.__type)
    
    def __eq__(self, other_node):
        if ((other_node.getPos() == self.getPos()) and (other_node.getType() == self.getType())):
            return True
        
        else:
            return False