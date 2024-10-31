import random
import NodeMap.Node as NODE

CONNECTION_CHANCE = 75

def randomizeNodeMap(node_map):
    node_map.reset()
    data = open("RANDOMIZATION_OPTIONS.txt", "r").read().split("\n")
    percentages = []

    # PRESET NODES
    node_map.setCell(0, 2, "EXPLORATION")
    node_map.setCell(6, 1, "SHOP")
    node_map.setCell(6, 3, "SHOP")
    node_map.setCell(7, 2, "BOSS")

    for i in range(1,len(data)-2):
        randomizeColumn(node_map, i, data[i])
        while not checkColumnForward(node_map, i-1):
            randomizeColumn(node_map, i, data[i])
    
    randomizeConnections(node_map)


def randomizeConnections(node_map):
    # 0 (Start Node)
    nodes = getNodesInColumn(node_map, 1)
    for node in nodes:
        if node.exists():
            node_map.drawConnection((0, 2, node.getX(), node.getY()))
    
    # The rest of them
    for i in range(1, 6):
        left  = getNodesInColumn(node_map, i)
        right = getNodesInColumn(node_map, i+1)
        connectColumns(node_map, left, right)
    
    for i in range(1,6):
        for node in getNodesInColumn(node_map, i):
            doubleCheckNode(node_map, node)

    # 6 (Shops to Boss)
    node_map.drawConnection((6, 1, 7, 2))
    node_map.drawConnection((6, 3, 7, 2))


def doubleCheckNode(node_map, node):
    nodes_behind = getNodesBehind(node_map, node)
    while not node_map.isConnectedTo(node):
        potential_node = random.choice(nodes_behind)
        if node_map.connectionValid((potential_node, node)):
            node_map.drawConnection((potential_node, node))
    
    nodes_ahead = getNodesAhead(node_map, node)
    while not node_map.hasConnectionFrom(node):
        potential_node = random.choice(nodes_ahead)
        if node_map.connectionValid((node, potential_node)):
            node_map.drawConnection((node, potential_node))

def getNodesBehind(node_map, node):
    to_test = []
    if node.getY() == 0:
        to_test = [0, 1]
    elif node.getY() == 4:
        to_test = [3, 4]
    else:
        to_test = [node.getY()-1, node.getY(), node.getY()+1]
    
    nodes = []
    for i in to_test:
        if node_map.getCell(node.getX()-1, i).exists():
            nodes.append(node_map.getCell(node.getX()-1, i))
    
    return nodes


def getNodesAhead(node_map, node):
    to_test = []
    if node.getY() == 0:
        to_test = [0, 1]
    elif node.getY() == 4:
        to_test = [3, 4]
    else:
        to_test = [node.getY()-1, node.getY(), node.getY()+1]
    
    nodes = []
    for i in to_test:
        if node_map.getCell(node.getX()+1, i).exists():
            nodes.append(node_map.getCell(node.getX()+1, i))
        
    
    return nodes


def connectColumns(node_map, left_side, right_side):
    for node_left in left_side:
        for node_right in right_side:
            if not areNodesAdjacent(node_left, node_right):
                continue
            
            # 75% chance connection is created
            if random.randint(0, 100) < CONNECTION_CHANCE:
                continue

            if not node_map.connectionValid((node_left, node_right)):
                continue

            node_map.drawConnection((node_left, node_right))

    
def areNodesAdjacent(n1, n2):
    if abs(n1.getY() - n2.getY()) < 2:
        return True
    return False


def getNodesInColumn(node_map, col_idx):
    nodes = []
    for i in range(5):
        if node_map.getCell(col_idx, i).exists():
            nodes.append(node_map.getCell(col_idx, i))
    
    return nodes


def checkColumnForward(node_map, col_idx):
    for y in range(5):
        #print(f"CHECKING ({col_idx}, {y})")
        if not (node_map.getCell(col_idx, y).exists()):
            continue

        valid = False
        
        if y == 0:
            to_check = [0, 1]
        elif y == 4:
            to_check = [3, 4]
        else:
            to_check = [y-1, y, y+1]
        
        for forward_y in to_check:
            if (node_map.getCell(col_idx+1, forward_y).exists()):
                valid = True
        
        if not valid:
            return False
    return True


def checkColumn(node_map, col_idx):
    for y in range(5):
        if type(node_map.getCell(col_idx, y) is not NODE.Node):
            continue

        valid = False
        
        if y == 0:
            to_check = [0, 1]
        elif y == 4:
            to_check = [3, 4]
        else:
            to_check = [col_idx-1, col_idx, col_idx+1]
        
        for previous_y in to_check:
            if type(node_map.getCell(col_idx-1, previous_y)) is NODE.Node:
                valid = False

        if not valid:
            return False
        

def randomizeColumn(node_map, col_idx, rules):
    room_weights, amount_weights = rules.split(";")

    room_weights = room_weights.split(" ")
    amount_weights = amount_weights.split(" ")

    amount = 0

    # Set Amount
    if amount_weights[0] == "P":
        amount = countNodesInColumn(node_map, col_idx-1) + random.randint(0,1)
    else:
        amount = int(chooseRandomFromWeights(amount_weights))
    
    if col_idx == 1:
        possible_idxs = [1, 2, 3]
    else:
        possible_idxs = [0, 1, 2, 3, 4]
    while amount > 0:
        if len(possible_idxs) > 1:
            potential_idx = possible_idxs.pop(random.randint(0,len(possible_idxs)-1))
        else:
            potential_idx = possible_idxs[0]
        #print("Checking (" + str(col_idx) + ", " + str(potential_idx) + ")")
        if checkValidityOfCell(node_map, col_idx, potential_idx):
            #print("Yep!")
            node_map.setCell(col_idx,
                             potential_idx,
                             chooseRandomFromWeights(room_weights))
            amount = amount - 1
                #break
            #else:
                #print("Nope.")


    #print(weights)
    #print(amount)
def checkValidityOfCell(node_map, x, y):
    to_check = []
    if y == 0:
        to_check = [0, 1]
    elif y == 4:
        to_check = [3, 4]
    else:
        to_check = [y-1, y, y+1]
    
    for prev_y in to_check:
        if node_map.getCell(x-1, prev_y).exists():
            return True

    return False

def chooseRandomFromWeights(raw_weights):
    total = 0
    amount = 0

    choice = random.randint(1, 100)

    # Setup weight dictionary
    for i in range(len(raw_weights) // 2):
        total = total + int(raw_weights[i*2+1])
        if choice <= total:
            return raw_weights[i*2]


def countNodesInColumn(node_map, col_idx):
    amount = 0
    for i in range(5):
        if (node_map.getCell(col_idx, i).exists()):
            amount = amount + 1
    
    return amount