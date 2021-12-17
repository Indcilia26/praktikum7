# praktikum7

## Tugas pemograman pertemuan 12 - Mengaplikasikan diagram class

================================

= Nama : Indira Rully Pricilia

= NIM : 312110354

= Kelas : TI.21.CA.1

=================================

### Latihan
Berikut soal latihan yang diberikan dosen :

![img](Screenshot/ss1.png)

dan ini hasil dari source code diatas :
```ruby
print("________________________________________")

#mengubah function menggunakan lambda
def a(x):
    return x ** 2

lambda x: x ** 2

print("1. Mengubah function menggunakan Lambda \n   def a(x): \n \t   return x ** 2")
print("   Hasil : lambda x: x ** 2")

def b(x, y):
    return math.sqrt(x ** 2 + y ** 2)

lambda x, y: math.sqrt(x ** 2 + y ** 2)

print("________________________________________")
print("2. Mengubah function menggunakan Lambda \n   def b(x, y): \n \t   return math.sqrt(x ** 2 + y ** 2)")
print("   Hasil : lambda x, y: math.sqrt(x ** 2 + y ** 2))")

def c(*args):
    return sum(args) / len(args)

lambda *args: sum(args) / len(args)

print("________________________________________")
print("3. Mengubah function menggunakan Lambda \n   def c(*args): \n \t   return sum(args) / len(args)")
print("   Hasil : lambda *args: sum(args) / len(args))")

def d(s):
    return "".join(set(s))

lambda s: "".join(set(s))

print("________________________________________")
print("4. Mengubah function menggunakan Lambda \n   def d(s): \n \t   return "".join(set(s))")
print("   Hasil : lambda s: "".join(set(s)))")
```

Berikut outputnya:

![img](Screenshot/ss1.png)

### Tugas Praktikum
Berikut soal yang diberikan dosen :

![img](Screenshot/ss1.png)

Inilah source code dari program saya :
```ruby
## Indirarully
data = {}

def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t\t: "))
    tugas = int(input("NIlai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


def tampilkan():
    if data.items():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("_______________________________________________________________________________________")
        print("|  No  |      NIM      |      NAMA         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
        print("|______|_______________|___________________|____________|_________|_________|________|__")
        i = 0
        for a in data.items():
            i += 1
            print(f"| {i:4} | {a[0]:13s} | {a[1][0]:17} | {a[1][1]:10d} |  {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("_______________________________________________________________________________________")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("_______________________________________________________________________________________")
        print("|      |               |             Tidak Ada Data         |         |                |")
    print("____________________________________________________________________________________________")


def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("===| BERHASIL MENGHAPUS DATA |===")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Data {0} tidak ada".format(nama))


def ubah():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("===| Edit Data Nilai Mahasiswa |===")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    nama = input("Masukan Nama\t\t: ")
    print("___________________________________")
    if nama in data.keys():
        nim = input("NIM baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("<><><><><><><><><><><><><><><><>")
        print("====| BERHASIL MENGUBAH DATA |====")
        print("<><><><><><><><><><><><><><><><>")
    else:
        print("Data nilai {0} tidak ada ".format(nama))


while True:
    print("")
    print("|_<><><><><><><><><><><><><><><><><>_|")
    print("|~~~~~~~~| DATA MAHASISWA |~~~~~~~~~~|")
    print("|_<><><><><><><><><><><><><><><><><>_|")
    x = input("1.| Lihat Data \n2.| Tambah Data \n3.| Ubah Data \n4.| Hapus Data \n0.| Keluar Aplikasi \nPilih menu : ")
    if x.lower() == "1":
        tampilkan()
    elif x.lower() == "2":
        tambah()
    elif x.lower() == "3":
        ubah()
    elif x.lower() == "4":
        hapus()
    elif x.lower() == "0":
        print()
        print("<><><><><><><><><><><><><><><><>")
        print("====== KELUAR DARI PROGRAM ======")
        print("<><><><><><><><><><><><><><><><>")
        break

    else:
        print()
        print("<><><><><><><><><><><><><><><><>")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("<><><><><><><><><><><><><><><><>")
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

System akan menjalankan fitur ini ketika user mengetikkan perintah 2 pada pilihan Pilih Menu (1-2-3-4-5) Inilah tampilan fitur Lihat Data :

![img](Screenshot/ss1.png)

**2) Menambahkan Data**

![img](Screenshot/ss1.png)

**3) Fitur ubah data**

Pada fitur ini user akan diminta untuk memilih data siapa yang akan diubah dan data apa yang akan dirubah Setelah user memilih data

![img](Screenshot/ss1.png)

**4) Fitur Hapus Data Nilai Mahasiswa**

System akan menjalankan fitur ini ketika user mengetikkan perintah 4 pada pilihan Pilih Menu (1-2-3-4-5)

![img](Screenshot/ss1.png)

Flowchart
Dan berikut adalah Hasil Dari Flowchartnya

![img](Screenshot/ss1.png)

*Sekian penjelasan praktikum 7, terimakasih atas perhatiannya..*

#### Indira Rully Pricilia - 312110354 - TI.21.CA.1
