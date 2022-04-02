from os.path import exists
import numpy as np
from queue_node import QueueNode
from node import Node
import time

class Puzzle:
    def __init__(self):
        self.matriks = self.getInput()
        self.totalKurang = self.kurang()
        self.solution = []
        self.banyakSimpul = 1
        self.route = []
        self.visited = set()

    def getInput(self):
        print("Pilih metode masukan data:")
        print("1. Matriks Random")
        print("2. Input File")

        choice = int(input("Masukkan pilihan: "))
        while (choice < 1 or choice > 2 or type(choice) != int):
            print("Pilihan tidak valid")
            choice = int(input("Masukan pilihan: "))
        matriks = []
        if choice == 1:
            temp = np.random.permutation(np.arange(1, 17))
            temp = np.ndarray.tolist(temp)
            matriks.append(temp[0:4])
            matriks.append(temp[4:8])
            matriks.append(temp[8:12])
            matriks.append(temp[12:16])
        else:
            filename = input("Masukkan nama file: ")
            filename = "../test/" + filename
            while not exists(filename):
                print("File tidak ditemukan")
                filename = input("Masukkan nama file: ")
                filename = "../test/" + filename

            f = open(filename, "r")
            matriks = [[int(num) for num in line.strip("\n").split(" ")] for line in f]
        
        return matriks

    def kurang(self):
        row = 0
        col = 0
        for i in range(4):
            for j in range(4):
                if self.matriks[i][j] == 16:
                    row = i
                    col = j
                    break

        total = 0
        for i in range(16):
            for j in range(i+1,16):
                if (self.matriks[j//4][j%4] < self.matriks[i//4][i%4]):
                    total += 1
        
        if ((row+col)%2 == 1):
            total += 1
        return total

    def solve(self):
        start = Node(self.matriks)
        queue = QueueNode()
        queue.push(start)
        while (not queue.isEmpty()):
            current = queue.pop()
            # print("Current: ", current.depth, ",", current.cost)
            hashedMat = np.array(current.matriks).tobytes()
            if (hashedMat in self.visited):
                continue
            else:
                self.visited.add(hashedMat)

            if (current.isGoal()):
                self.solution.append(current)
                queue.kill(current.cost)
            else:
                child = current.getChildren()
                self.banyakSimpul += len(child)
                for node in child:
                    queue.push(node)

    def findRoute(self):
        result = self.solution[0]
        while (result.parent != None):
            self.route.append(result)
            result = result.parent
        self.route.reverse()

    def printResult(self):
        for i in range(len(self.route)):
            print()
            print("Langkah ke-", i+1, ": ", self.route[i].getLastRoute())
            self.route[i].printMatriks()
        
        print("\nJumlah simpul yang dibangkitkan: ", self.banyakSimpul)

    def printMatriks(self):
        for i in range(4):
            for j in range(4):
                print(self.matriks[i][j], end = " ") if self.matriks[i][j] != 16 else print("#", end = " ")
            print()

game = Puzzle()
print("Konfigurasi game:")
game.printMatriks()

# check Kurang(i) + X
print("\nTotal Kurang + X : " + str(game.kurang()))
# jika Kurang(i) + X ganjil makan tidak ada solusi
if (game.kurang()%2 == 1):
    print("Puzzle tidak dapat diselesaikan")
else:
    print("Puzzle dapat diselesaikan")
    # Memulai timer
    start = time.process_time_ns()

    # Solve puzzle
    game.solve()
    
    # Mencari route dari solusi yang ditemukan
    game.findRoute()

    # Mengakhiri timer
    end = time.process_time_ns()
    duration = end - start

    # Menampilkan hasil
    game.printResult()
    print("Total Pergeseran: ", len(game.route))
    print("Waktu eksekusi: ", duration/1000000, " ms")