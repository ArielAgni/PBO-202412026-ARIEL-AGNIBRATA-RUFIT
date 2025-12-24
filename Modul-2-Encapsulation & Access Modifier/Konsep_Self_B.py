class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# Membuat 2 Mata Kuliah
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Basis Data")

# Membuat 3 Mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# Mendaftarkan mahasiswa ke masing-masing mata kuliah
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)
mk1.tambah_mahasiswa(m3)

mk2.tambah_mahasiswa(m1)
mk2.tambah_mahasiswa(m3)

# Menampilkan hasil
print("Daftar Mahasiswa di", mk1.nama, ":", mk1.daftar_mahasiswa())
print("Jumlah:", mk1.jumlah_mahasiswa())

print("Daftar Mahasiswa di", mk2.nama, ":", mk2.daftar_mahasiswa())
print("Jumlah:", mk2.jumlah_mahasiswa())
