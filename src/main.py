from os.path import exists
import numpy as np
from queue_node import QueueNode
from node import Node
import time

class Puzzle:
    # Constructor
    def __init__(self):
        self.matriks = self.getInput()
        self.EmptyRow = 0
        self.EmptyCol = 0
        self.cost = 0
        self.kurang = []
        self.totalKurang = 0
        self.solution = []
        self.route = []
        self.visited = set()
        self.banyakSimpul = 1
        self.kalkulasi()

    # Method untuk mendapatkan input matriks
    def getInput(self):
        print("Pilih metode masukan data:")
        print("1. Matriks Random")
        print("2. Input File")

        # Pilihan input
        choice = int(input("Masukkan pilihan: "))
        while (choice < 1 or choice > 2 or type(choice) != int):
            print("Pilihan tidak valid")
            choice = int(input("Masukan pilihan: "))
        matriks = []

        if choice == 1:
        # Input matriks secara random
            temp = np.random.permutation(np.arange(1, 17))
            temp = np.ndarray.tolist(temp)

            # Menyalin list ke dalam matriks
            matriks.append(temp[0:4])
            matriks.append(temp[4:8])
            matriks.append(temp[8:12])
            matriks.append(temp[12:16])
        else:
        # Input matriks dari file
            filename = input("Masukkan nama file: ")
            while not exists(filename):
                print("File tidak ditemukan")
                filename = input("Masukkan nama file: ")

            f = open(filename, "r")
            # Menyalin isi file ke dalam matriks
            matriks = [[int(num) for num in line.strip("\n").split(" ")] for line in f]
        
        return matriks

    # Method untuk melakukan kalkulasi sum kurang dan cost matriks awal
    def kalkulasi(self):
        # Perulangan untuk mencari sel kosong dan menghitung cost
        for i in range(4):
            for j in range(4):
                if self.matriks[i][j] == 16:
                    self.EmptyRow = i
                    self.EmptyCol = j
                else:
                    self.cost += (self.matriks[i][j] != i*4 + j + 1)

        # Perulangan untuk mencari tabel kurang
        for i in range(16):
            temp = 0
            for j in range(i+1,16):
                if (self.matriks[j//4][j%4] < self.matriks[i//4][i%4]):
                    temp += 1
            self.kurang.append(temp)
        
        # if ((self.EmptyRow+self.EmptyCol)%2 == 1):
        #     self.totalKurang += 1

    # Method untuk menyelesaikan puzzle
    def solve(self):
        # Inisialisasi root node
        start = Node(self.matriks, self.cost, self.EmptyRow, self.EmptyCol)
        queue = QueueNode()
        queue.push(start)
        
        # Perulangan untuk mencari solusi
        while (not queue.isEmpty()):
            current = queue.pop()
            # print("Current: ", current.depth, ",", current.cost)

            # Mengecek apakah sebuah matriks sudah pernah dicek atau belum
            if (np.array(current.matriks).tobytes() in self.visited):
                continue
            else:
                self.visited.add(np.array(current.matriks).tobytes())

            if (current.isGoal()):
            # Cek apakah node ini merupakan goal node
                self.solution.append(current)
                queue.kill(current.cost)
                break
            else:
            # Jika bukan goal node, bangkitkan anak-anak berdasarkan node yang dicek
                child = current.getChildren()
                self.banyakSimpul += len(child)
                for node in child:
                    queue.push(node)

    # Method untuk mencari rute dari sebuah solusi yang ditemukan
    def findRoute(self):
        result = self.solution[0]
        while (result.parent != None):
            self.route.append(result)
            result = result.parent
        self.route.reverse()

    # Method untuk mencetak langkah-langkah penyelesaian
    def printResult(self):
        for i in range(len(self.route)):
            print()
            print("Langkah ke-", i+1, ": ", self.route[i].getLastRoute())
            self.route[i].printMatriks()
        
        print("\nJumlah simpul yang dibangkitkan: ", self.banyakSimpul)

    # Method untuk mencetak matriks
    def printMatriks(self):
        for i in range(4):
            for j in range(4):
                print(self.matriks[i][j], end = " ") if self.matriks[i][j] != 16 else print("#", end = " ")
            print()

# ======== MAIN PROGRAM ======== #
game = Puzzle()
print("Konfigurasi game:")
game.printMatriks()

# Mencetak tabel kurang
print("Tabel kurang:")
for i in range(8):
    print(i+1, ": ", game.kurang[i], "\t", i+8, ": ", game.kurang[i+8])
print("X: ", (game.EmptyRow+game.EmptyCol)%2)

# check Kurang(i) + X
print("\nTotal Kurang + X : " + str(sum(game.kurang) + (game.EmptyRow+game.EmptyCol)%2))
# Jika Kurang(i) + X ganjil makan tidak ada solusi
if (game.totalKurang%2 == 1):
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