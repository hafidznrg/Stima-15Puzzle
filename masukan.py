from os.path import exists
import numpy as np

def getInput():
    print("Pilih metode masukan data:")
    print("1. Matriks Random")
    print("2. Input File")

    choice = int(input("Masukkan pilihan: "))
    while (choice < 1 or choice > 2):
        print("Pilihan tidak valid")
        choice = int(input("Masukan pilihan: "))
    matriks = []
    if choice == 1:
        temp = np.random.permutation(np.arange(0, 16))
        temp = np.ndarray.tolist(temp)
        matriks.append(temp[0:4])
        matriks.append(temp[4:8])
        matriks.append(temp[8:12])
        matriks.append(temp[12:16])
    else:
        filename = input("Masukkan nama file: ")
        while not exists(filename):
            print("File tidak ditemukan")
            filename = input("Masukkan nama file: ")

        f = open(filename, "r")
        matriks = [[int(num) for num in line.strip("\n").split(" ")] for line in f]
    
    return matriks