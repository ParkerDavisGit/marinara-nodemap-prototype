class Node:
    def __init__(self):
        self.__x      = 0
        self.__y      = 0
        self.__type   = ""
        self.__exists = False
    
    #=====[ GETTERS ]==========
    def getPos(self):
        return (self.__x, self.__y)
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getType(self):
        return self.__type

    def exists(self):
        return self.__exists

    #=====[ SETTERS ]==========
    def at(self, x, y):
        self.__x = x
        self.__y = y
        return self
    
    def ofType(self, new_type):
        self.__type = new_type
        return self

    def isReal(self):
        self.__exists = True
        return self

    #=====[ DUNDER ZONE ]==========
    def __str__(self):
        return f"{self.__type}"
    
    def __deepcopy__(self):
        return Node().at(self.__x, self.__y).ofType(self.__type)
    
    def __eq__(self, other_node):
        if ((other_node.getPos() == self.getPos()) and (other_node.getType() == self.getType())):
            return True
        
        else:
            return False