# Tugas Kecil 3 IF2211 Strategi Algoritma
Penyelesaian Persoalan 15-Puzzle dengan Algoritma Branch and Bound

## Deskripsi
Program ini dibuat untuk memenuhi Tugas Kecil 3 IF2211 Strategi Algoritma. Program ini bertujuan untuk menyelesaikan sebuah persoalan 15-puzzle dengan menggunakan Algoritma Branch and Bound. Program ini menggunakan metode misplaced tiles untuk menghitung cost dari setiap simpul. Program ini dapat menyelesaikan persoalan dengan cukup cepat apabila jumlah pergerakan yang diperlukan bernilai kurang dari 30. Apabila lebih besar dari 30, program membutuhkan waktu yang cukup lama untuk menyelesaikan persoalan. Program ini sudah dioptimalisasi dengan menggunakan heapq untuk menyimpan queue simpul yang akan diperiksa dan menggunakan set untuk menyimpan susunan matriks yang sudah diperiksa.

## Fitur
- Program ini dapat menerima input matriks dari sebuah file atau sebuah matriks random.
- Program ini dapat menampilkan nilai fungsi kurang(i) pada susunan matriks yang diberikan.
- Program ini dapat menyelesaikan persoalan 15-puzzle dengan menggunakan Algoritma Branch and Bound.
- Program ini dapat menampilkan urutan langkah penyelesaian persoalan 15-puzzle.
- Program ini dapat menampilkan waktu yang dibutuhkan untuk menyelesaikan persoalan 15-puzzle.
- Program ini dapat menampilkan total simpul yang dibangkitkan dalam menyelesaikan persoalan 15-puzzle.

## Requirement
Program ini membutuhkan Python versi 3.10 ke atas dan membutuhkan library numpy. Sebagai referensi, penulis menggunakan Python versi 3.10.2 dan library numpy versi 1.22.2.

## Cara Penggunaan Program
1. Clone repository ini ke dalam folder lokal Anda
2. Jalankan main program dengan menjalankan perintah ```py src/main.py```
3. Masukan pilihan 1 apabila ingin menggunakan input berupa matriks random, pilihan 2 apabila ingin menggunakan input matriks yang berasal dari file.
4. Jika memilih pilihan 2, masukkan nama file yang berisi matriks yang ingin diinput. Di dalam repository ini terdapat beberapa contoh file matriks yang berada dalam folder ```test```. Untuk menggunakannya, Anda bisa memasukkan perintah ```test/<nama_file>.txt```.
5. Tunggu program dalam menyelesaikan persoalan 15-puzzle.

## Pembuat
Program ini dibuat oleh:
<br>
Nama    : Hafidz Nur Rahman Ghozali
<br>
NIM     : 13520117