from enum import Enum

class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

class Node:
    def __init__(self, matriks, route = [], parent = None, depth = 0):
        self.matriks = matriks
        self.route = route
        self.parent = parent
        self.depth = depth
        self.cost = self.calculateCost()
        self.x, self.y = self.getEmptyCell()
    
    def calculateCost(self):
        if self.depth == 0:
            return 0
        cost = 0
        for i in range(16):
            if (self.matriks[i // 4][i % 4] != 0 and self.matriks[i // 4][i % 4] != i + 1):
                cost += 1
        cost += self.depth
        return cost
    
    def print(self):
        print("Route: ", self.route)
        print("Parent: " + str(self.parent))
        print("Depth: " + str(self.depth))
        print("Cost: " + str(self.cost))
        self.printMatriks()
    
    def isGoal(self):
        isGoal = True
        for i in range(15):
            if (self.matriks[i // 4][i % 4] != i + 1):
                isGoal = False
                break
        return isGoal

    def getEmptyCell(self):
        for i in range(4):
            for j in range(4):
                if self.matriks[i][j] == 16:
                    return i, j
    
    def moveEmptyCell(self, direction):
        if direction == Direction.UP:
            if (self.x > 0 and (self.route == [] or self.route[-1] != Direction.DOWN)):
                return self.move(self.x, self.y, -1, 0)
        elif direction == Direction.DOWN:
            if (self.x < 3 and (self.route == [] or self.route[-1] != Direction.UP)):
                return self.move(self.x, self.y, 1, 0)
        elif direction == Direction.LEFT:
            if (self.y > 0 and (self.route == [] or self.route[-1] != Direction.RIGHT)):
                return self.move(self.x, self.y, 0, -1)
        elif direction == Direction.RIGHT:
            if (self.y < 3 and (self.route == [] or self.route[-1] != Direction.LEFT)):
                return self.move(self.x, self.y, 0, 1)
        
        return None

    def move(self, x, y, dx, dy):
        temp = [[num for num in row] for row in self.matriks]
        temp[x][y], temp[x + dx][y + dy] = temp[x + dx][y + dy], temp[x][y]
        return temp
    
    def getChildren(self):
        children = []
        for direction in Direction:
            child = self.moveEmptyCell(direction)
            if child != None:
                children.append(Node(child, self.route + [direction], self, self.depth + 1))
        return children

    def printMatriks(self):
        for i in range(4):
            for j in range(4):
                print(self.matriks[i][j], end = " ") if self.matriks[i][j] != 16 else print("#", end = " ")
            print()

    def getLastRoute(self):
        match self.route[-1]:
            case Direction.UP:
                return "UP"
            case Direction.DOWN:
                return "DOWN"
            case Direction.LEFT:
                return "LEFT"
            case Direction.RIGHT:
                return "RIGHT"
        return None

    def __lt__(self, other):
        if (self.cost == other.cost):
            return self.depth > other.depth
        return self.cost < other.cost