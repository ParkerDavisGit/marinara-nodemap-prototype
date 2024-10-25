import random
import NodeMap.Node as NODE

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
    nodes = getNodesInColumn(node_map, 1, False)
    for node in nodes:
        node_map.drawConnection((0, 2, node.getX(), node.getY()))
    
    # The rest of them
    for i in range(1, 6):
        left  = getNodesInColumn(node_map, i  , True)
        right = getNodesInColumn(node_map, i+1, True)
        connectColumns(node_map, left, right)

    # 6 (Shops to Boss)
    node_map.drawConnection((6, 1, 7, 2))
    node_map.drawConnection((6, 3, 7, 2))

def connectColumns(node_map, left_side, right_side):
    topL = 0
    topR = 0
    botL = 4
    botR = 4

    while ((type(left_side[topL]) != NODE.Node)):
        topL = topL + 1
    while (type(right_side[topR]) != NODE.Node):
        topR = topR + 1
    while ((type(left_side[botL]) != NODE.Node)):
        botL = botL - 1
    while (type(right_side[botR]) != NODE.Node):
        botR = botR - 1
    
    node_map.drawConnection((left_side[topL].getX(), left_side[topL].getY(),
                            right_side[topR].getX(), right_side[topR].getY()))

    node_map.drawConnection((left_side[botL].getX(), left_side[botL].getY(),
                            right_side[botR].getX(), right_side[botR].getY()))
    
    # Nodes going straight across
    for node in left_side:
        if (type(node) != NODE.Node):
            continue
        if (type(right_side[node.getY()]) == NODE.Node):
            node_map.drawConnection((node.getX(), node.getY(),
                                     node.getX()+1, node.getY()))


def getNodesInColumn(node_map, col_idx, pad):
    nodes = []
    for i in range(5):
        if (type(node_map.getCell(col_idx, i)) == NODE.Node):
            nodes.append(node_map.getCell(col_idx, i))
        elif pad:
            nodes.append("x")
    
    return nodes


def checkColumnForward(node_map, col_idx):
    for y in range(5):
        #print(f"CHECKING ({col_idx}, {y})")
        if not (type(node_map.getCell(col_idx, y)) is NODE.Node):
            continue

        valid = False
        
        if y == 0:
            to_check = [0, 1]
        elif y == 4:
            to_check = [3, 4]
        else:
            to_check = [y-1, y, y+1]
        
        for forward_y in to_check:
            if (type(node_map.getCell(col_idx+1, forward_y)) is NODE.Node):
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
        potential_idx = possible_idxs.pop(random.randint(0,len(possible_idxs)-1))
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
        if type(node_map.getCell(x-1, prev_y)) is NODE.Node:
            #print(f"Found!: {node_map.getCell(x-1, prev_y)} @ ({x-1}, {prev_y})")
            return True
        #else:
            #print(f"Stupid Stupid: {node_map.getCell(x-1, prev_y)} @ ({x-1}, {prev_y})")

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
        if (type(node_map.getCell(col_idx, i)) == NODE.Node):
            amount = amount + 1
    
    return amount