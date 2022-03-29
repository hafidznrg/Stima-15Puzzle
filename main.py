from masukan import getInput
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Node:
    def __init__(self, matriks, route = [], parent = None, depth = 0):
        self.matriks = matriks
        self.route = route
        self.parent = parent
        self.depth = depth
        self.cost = self.calculateCost()
        self.x, self.y = self.getZero()
    
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
        printMatriks(self.matriks)
    
    def isGoal(self):
        isGoal = True
        for i in range(15):
            if (self.matriks[i // 4][i % 4] != i + 1):
                isGoal = False
                break
        
        return isGoal

    def getZero(self):
        for i in range(4):
            for j in range(4):
                if self.matriks[i][j] == 0:
                    return i, j
    
    def moveZero(self, direction):
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
            child = self.moveZero(direction)
            if child != None:
                children.append(Node(child, self.route + [direction], self, self.depth + 1))
        return children

class QueueNode:
    def __init__(self):
        self.queue = []

    def push(self, node):
        if (self.length() == 0):
            self.queue.append(node)
        else:
            for i in range(self.length()):
                if (node.cost < self.queue[i].cost):
                    self.queue.insert(i, node)
                    break
                elif (i == self.length() - 1):
                    self.queue.append(node)

    def pop(self):
        return self.queue.pop(0)
    
    def length(self):
        return len(self.queue)

    def kill(self, cost):
        i = 0
        while (i < self.length()):
            if (self.queue[i].cost > cost):
                self.queue.pop(i)
            else:
                i += 1

    def print(self):
        for node in self.queue:
            node.print()

def hitungKurang(matriks):
    row = 0
    col = 0
    for i in range(4):
        for j in range(4):
            if matriks[i][j] == 0:
                row = i
                col = j
                break

    total = 0
    matriks[row][col] = 16
    for i in range(16):
        for j in range(i+1,16):
            if (matriks[j//4][j%4] < matriks[i//4][i%4] and matriks[j//4][j%4] != 0):
                total += 1
    
    if ((row+col)%2 == 1):
        total += 1
    matriks[row][col] = 0
    return total

def calculateCost(matriks):
    total = 0
    for i in range(16):
        if (matriks[i // 4][i % 4] != 0 and matriks[i // 4][i % 4] != i + 1):
            total += 1
    return total

def run(matriks):
    # check Kurang(i) + X
    sumKurang = hitungKurang(matriks)

    print("Total : " + str(sumKurang))

    # jika Kurang(i) + X ganjil makan tidak ada solusi
    if (sumKurang%2 == 1):
        print("Puzzle tidak dapat diselesaikan")
        return
    
    # Nasuk ke algoritma Branch and Bound
    queue = QueueNode()
    queue.push(Node(matriks))
    banyakSimpul = 1
    solution = None

    # Masuk perulangan
    print("Masuk perulangan")
    while queue.length() > 0:
        node = queue.pop()
        if node.isGoal():
            solution = node
            queue.kill(node.cost)
        else:
            child = node.getChildren()
            banyakSimpul += len(child)
            for i in range(len(child)):
                queue.push(child[i])
    
    rute = []
    if (solution != None):
        rute.append(solution)
        print("Banyak simpul yang dibangkitkan: " + str(banyakSimpul))
        # print("Rute yang digunakan: " + str(solution.route))
        iterator = solution.parent
        while (iterator != None):
            rute.insert(0, iterator)
            iterator = iterator.parent

    print("=============")
    for i in range(len(rute)):
        printMatriks(rute[i].matriks)
        print("=============")

def printMatriks(matriks):
    for line in matriks:
        for elem in line:
            print(elem, end=" ")
        print()

matriks = getInput()
print("Matriks awal:")
printMatriks(matriks)
run(matriks)