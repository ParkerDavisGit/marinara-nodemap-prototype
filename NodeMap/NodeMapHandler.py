import NodeMap.NodeMap as NODEMAP

class NodeMapHandler:
    def __init__(self, node_surface, connection_surface):
        self.__node_map = NODEMAP.NodeMap(node_surface, connection_surface)
    

    def __str__(self):
        return self.__node_map.__str__()