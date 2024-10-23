import NodeMap.NodeMap as NODEMAP

class NodeMapHandler:
    def __init__(self):
        self.__node_map = nodemap.NodeMap()
    

    def __str__(self):
        return self.__node_map.__str__()