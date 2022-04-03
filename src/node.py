from enum import Enum

class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

class Node:
    # Constructor
    def __init__(self, matriks, cost, emptyRow, emptyCol, route = [], parent = None, depth = 0):
        self.matriks = matriks
        self.route = route
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.emptyRow = emptyRow
        self.emptyCol = emptyCol
    
    # Method print untuk mencetak info node, untuk pengecekan
    def print(self):
        print("Route: ", self.route)
        print("Parent: " + str(self.parent))
        print("Depth: " + str(self.depth))
        print("Cost: " + str(self.cost))
        self.printMatriks()
    
    # Method untuk mengecek apakah merupakan goal node
    def isGoal(self):
        return self.matriks == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    # Method untuk membangkitkan anak-anak dari suatu node
    def getChildren(self):
        children = []

        # Iterasi pada arah yang dapat dilalui
        for direction in Direction:
            # Menyalin informasi dari parent
            childMat = [[num for num in row] for row in self.matriks]
            childRoute = self.route + [direction]
            newEmptyRow = self.emptyRow
            newEmptyCol = self.emptyCol

            # Membandingkan arah yang dipilih
            match direction:
                case Direction.UP:
                    if (self.emptyRow > 0 and (self.route == [] or self.route[-1] != Direction.DOWN)):
                        newEmptyRow -= 1
                case Direction.DOWN:
                    if (self.emptyRow < 3 and (self.route == [] or self.route[-1] != Direction.UP)):
                        newEmptyRow += 1
                case Direction.LEFT:
                    if (self.emptyCol > 0 and (self.route == [] or self.route[-1] != Direction.RIGHT)):
                        newEmptyCol -= 1
                case Direction.RIGHT:
                    if (self.emptyCol < 3 and (self.route == [] or self.route[-1] != Direction.LEFT)):
                        newEmptyCol += 1
            
            # Jika arah yang dipilih vaid, tambahkan ke children
            if (self.emptyRow != newEmptyRow or self.emptyCol != newEmptyCol):
                # Menghitung misplaced pada susunan matriks baru
                misplaced = 0
                if (childMat[newEmptyRow][newEmptyCol] == self.emptyRow*4 + self.emptyCol + 1): misplaced -= 1
                childMat[self.emptyRow][self.emptyCol], childMat[newEmptyRow][newEmptyCol] = childMat[newEmptyRow][newEmptyCol], childMat[self.emptyRow][self.emptyCol]
                if (childMat[newEmptyRow][newEmptyCol] == self.emptyRow*4 + self.emptyCol + 1): misplaced += 1
                # Menambahkan node baru ke children
                children.append(Node(childMat, self.cost + misplaced + 1, newEmptyRow, newEmptyCol, childRoute, self, self.depth + 1))
        
        return children

    # Method untuk mencetak matriks
    def printMatriks(self):
        print("\t+-----+-----+-----+-----+")
        for i in range(4):
            print("\t|", end="")
            for j in range(4):
                if (self.matriks[i][j] == 16):
                    print("     |", end = "")
                elif (self.matriks[i][j] > 9):
                    print("  " + str(self.matriks[i][j]) + " |", end="")
                else:
                    print("  " + str(self.matriks[i][j]) + "  |", end="")
            print("\n\t+-----+-----+-----+-----+")

    # Method untuk mencetak langkah terakhir suatu node
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

    # Method overloading '<' untuk membantu heapq
    def __lt__(self, other):
        if (self.cost == other.cost):
            return self.depth > other.depth
        return self.cost < other.cost