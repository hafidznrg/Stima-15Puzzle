from tkinter import S
from masukan import getInput
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Node:
    def __init__(self, matriks, route = [], parent = None, depth = 0, cost = 0):
        self.matriks = matriks
        self.route = route
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.x, self.y = self.getZero()
    
    # def calculateCost(self):
    #     cost = 0
    #     for i in range(16):
    #         if (self.matriks[i // 4][i % 4] != 0 and self.matriks[i // 4][i % 4] != i + 1):
    #             cost += 1
    #     if (self.parent != None):
    #         cost += self.parent.cost
    #     return cost
    
    def print(self):
        print("Route: ", self.route)
        print("Parent: " + str(self.parent))
        print("Depth: " + str(self.depth))
        print("Cost: " + str(self.cost))
        printMatriks(self.matriks)
    
    def isGoal(self):
        isGoal = True
        for i in range(16):
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

    # jika Kurang(i) + X ganjil makan tidak ada solusi
    if (sumKurang%2 == 1):
        print("Tidak dapat mencapai solusi")
        return
    
    # Nasuk ke algoritma Branch and Bound
    queue = []
    queue.append(Node(matriks))
    solution = None

    # Masuk perulangan
    print("Masuk perulangan")
    while len(queue) > 0:
        node = queue.pop(0)
        node.print()
        if node.isGoal():
            print("Ditemukan sebuah solusi")
            solution = node
            # Masih perlu mematikan simpul yang memiliki cost lebih besar
        else:
            child = node.getChildren()
            for i in range(len(child)):
                child[i].cost = calculateCost(child[i].matriks)
                queue.append(child[i])
                print("Anak ke-" + str(i) + ":")
                child[i].print()
            
    

def printMatriks(matriks):
    for line in matriks:
        for elem in line:
            print(elem, end=" ")
        print()

matriks = getInput()
# print("Matriks awal:")
# printMatriks(matriks)
run(matriks)

# for direction in Direction:
#     print(direction)