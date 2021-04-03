import copy

# Node in the search tree
class boardState:
    """boardState class

    Defines the state of the 8-puzzle board, the parent node, the number of moves taken to get to this state and the cost of the state"""
    
    def __init__(self, state, n=0, p=None, c=0):
        self.state = state
        self.n = n # number of moves
        self.p = p # parent
        self.c = c # cost
    
    # String passed when print(boardState_obj) is called
    def __str__(self):
        return str(self.state)
    
    # String representation of the class (Used insted of "<< boardState object located at 0x000....... >>")
    def __repr__(self):
        return " << "+str(self.state)+" "+str(self.c)+" >> \n"

# Check if two states are equal
def statesEqual(s1, s2):
    for i1, i2 in zip(s1, s2):
        for j1, j2 in zip(i1, i2):
            if not j1 == j2:
                return False
    return True

# Heuristic value
def heuristic(c, g): # Current state, Goal
    h = 0 # Hamming distance
    for i, j in zip(c.state, g.state):
        for k, l in zip(i, j):
            if not (k == l):
                h = h + 1
    return h + c.n

# Check if child has occured before
def check(c):
    a = c.p # a is ancestor of c
    while not (a.p == None):
        if(statesEqual(c.state, a.p.state)):
            return True
        a = a.p
    return False

# Get coordinates of blank block
def coord(c, el = None):
    for i in range(len(c.state)):
        for j in range(len(c.state[0])):
            if c.state[i][j] == el:
                return (i, j)

# Generate children of current state
def generate(c, g):
    (x, y) = coord(c)
    children = []
    if not x == 0: # Up
        nState = copy.deepcopy(c.state)
        nState[x-1][y] = None
        nState[x][y] = c.state[x-1][y]
        child = boardState(nState, c.n + 1, c)
        child.c = heuristic(child, g)
        if not check(child):
            children.append(child)
    if not y == 0: # Left
        nState = copy.deepcopy(c.state)
        nState[x][y-1] = None
        nState[x][y] = c.state[x][y-1]
        child = boardState(nState, c.n + 1, c)
        child.c = heuristic(child, g)
        if not check(child):
            children.append(child)
    if not x == 2: # Down
        nState = copy.deepcopy(c.state)
        nState[x+1][y] = None
        nState[x][y] = c.state[x+1][y]
        child = boardState(nState, c.n + 1, c)
        child.c = heuristic(child, g)
        if not check(child):
            children.append(child)
    if not y == 2: # Right
        nState = copy.deepcopy(c.state)
        nState[x][y+1] = None
        nState[x][y] = c.state[x][y+1]
        child = boardState(nState, c.n + 1, c)
        child.c = heuristic(child, g)
        if not check(child):
            children.append(child)
    return children

# Get index of child with minimum cost
def qmin(q):
    minH = q[0].c
    minIdx = 0
    for idx, i in enumerate(q):
        if i.c < minH:
            minH = i.c
            minIdx = idx
    return minIdx

# Print current state
def printBoard(b):
    s = b.state
    for i in s:
        print(i)
    print()

""" # Lab question
initState = [[1,2,6],[7,5,3],[4,8,None]]
goalState = [[1,2,3],[4,5,6],[7,8,None]] """


# Sample question
initState = [[2,8,3],[1,6,4],[7,None,5]]
goalState = [[1,2,3],[8,None,4],[7,6,5]]


G = boardState(goalState)
S = boardState(initState)
S.c = heuristic(S, G)

if __name__ == '__main__':
    q = [S]
    traversed = []

    it = 0 # Number of iterations
    flag = False # Reached goal?
    goalNode = None

    while q:
        """print(q)"""
        s = q.pop(qmin(q))
        traversed.append(s)
        print("State ({0}) is: ".format(it))
        printBoard(s)
        """
        if not it == 0:
            print("Parent state:")
            printBoard(s.p)
        """
        if statesEqual(s.state, G.state):
            flag = True
            goalNode = s
            break
        q = q + generate(s, G)
        it += 1
    
    if flag:
        path = []
        s = goalNode
        while not s == None:
            path.append(s)
            s = s.p
        path.reverse()
        print("Path to Goal (Number of moves = {0}):".format(len(path)))
        for i in path:
            printBoard(i)

    if not flag:
        print("404! Solution not found.")