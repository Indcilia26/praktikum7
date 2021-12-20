# praktikum7

## Tugas pertemuan 12 - Mengaplikasikan diagram class

================================

= Nama  : Indira Rully Pricilia

= NIM   : 312110354

= Kelas : TI.21.CA.1

=================================

### Tugas Praktikum
Berikut soal praktikum yang diberikan dosen :

![img](Screenshot/ss1.png)

Inilah source code dari program saya :
```ruby
#include <iostream>
#Indirarully

int
class Mahasiswa:
     ''' Dasar kelas untuk nilai mahasiswa'''
     jumlah_mahasiswa = 0

     def __init__(self, nama, nim, nilai):
         self.nama  = nama
         self.nilai = nilai
         self.nim   = nim
         Mahasiswa.jumlah_mahasiswa += 1

     def tampilkan_jumlah(self):
         print("Total mahasiswa :" , Mahasiswa.jumlah_mahasiswa)

     def tampilkan_profil(self):
         print("Nama  :", self.nama)
         print("Nilai :", self.nilai)
         print("Nim   :", self.nim)

# Membuat objek pertama di kelas mhs
Mahasiswa1 = Mahasiswa("Indira", 90, 312110354)

# Membuat objek kedua di kelas mhs
Mahasiswa2 = Mahasiswa("Pricilia", 80, 31200000)

Mahasiswa1.tampilkan_profil()
Mahasiswa2.tampilkan_profil()

print("Total mahasiswa :", Mahasiswa.jumlah_mahasiswa)
```

Saat di run, maka program akan menghasilkan output ini :

![img](Screenshot/ss1.png)


Terdapat 5 Pilihan menu, yaitu :

= 1. Lihat Data

= 2. Tambah Data

= 3. Ubah Data

= 4. Hapus Data

= 0. Keluar Aplikasi


**1) Lihat Data Nilai Mahasiswa**

System akan menjalankan fitur ini ketika user mengetikkan perintah 1 pada pilihan Pilih Menu (1-2-3-4-5) Inilah tampilan fitur Lihat Data :

![img](Screenshot/ss1.png)

**2) Menambahkan Data**

Fitur ini akan menambahkan data berupa Nama, Nim dan nilai menggunakan menu perintah 2 pada menu 1-2-3-4-5, berikut outputnya :

![img](Screenshot/ss1.png)

**3) Fitur ubah data**

Pada fitur ini user akan diminta untuk memilih data siapa yang akan diubah dan data apa yang akan dirubah Setelah user memilih data

![img](Screenshot/ss1.png)

**4) Fitur Hapus Data Nilai Mahasiswa**

System akan menjalankan fitur ini ketika user mengetikkan perintah 4 pada pilihan Pilih Menu (1-2-3-4-5)

![img](Screenshot/ss1.png)


### Flowchart
Dan berikut adalah Hasil Dari Flowchartnya

![img](Screenshot/ss1.png)

*Sekian penjelasan praktikum 7, terimakasih atas perhatiannya..*

#### Indira Rully Pricilia - 312110354 - TI.21.CA.1
