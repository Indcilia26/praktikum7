
class mahasiswa():
      ''' Dasar kelas untuk nilai mahasiswa'''
      jumlah_mahasiswa = 0

     def __init__(self, nama, nilai, nim):
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

# Membuat objek di kelas mhs
Indira = mahasiswa('Indira, 90, 312110354')
Pricilia = mahasiswa('Pricilia, 87, 312000000')

    def cetak(self):
        print("\nNama: {}\nNilai: {}\.format(self.nama, self.nilai, self.nim)" )

print()
