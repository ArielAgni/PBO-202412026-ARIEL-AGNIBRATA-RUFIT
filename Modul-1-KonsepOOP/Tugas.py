class Mahasiswa:
    #attribute
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # M Perkenalan diri
    def perkenalan_diri(self):
        print(f"Halo, nama saya {self.nama}.")
        print(f"Saya dari jurusan {self.jurusan} dengan NIM {self.nim}.")
        print(f"Saya berasal dari {Mahasiswa.universitas}.")
        print()

    # M Update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} telah diperbarui menjadi {self.ipk}.")
        print()

    # M Predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"

# INSTANSIASI OBJECT

mhs1 = Mahasiswa("Ariel", "20241026", "Informatika", 3.6)
mhs2 = Mahasiswa("Herman", "270271025", "Sistem Informasi", 2.9)
mhs3 = Mahasiswa("Nanang", "270271024", "Teknik Komputer", 1.8)

mhs1.perkenalan_diri()

mhs1.update_ipk(3.8)
mhs2.update_ipk(3.1)
mhs3.update_ipk(2.2)

print("Predikat Kelulusan:")
print(f"{mhs1.nama} : {mhs1.predikat_kelulusan()}")
print(f"{mhs2.nama} : {mhs2.predikat_kelulusan()}")
print(f"{mhs3.nama} : {mhs3.predikat_kelulusan()}")
