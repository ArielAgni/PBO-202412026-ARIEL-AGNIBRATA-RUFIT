class Dosen:
    def __init__(self, nama, nidn, matkul):
        self.nama = nama
        self.nidn = nidn
        self.matkul = matkul

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIDN {self.nidn} Saya mengajar Matakuliah {self.matkul}"

# Pembuatan object
dsn1 = Dosen("Nanang", "12345","Matematika")
dsn2 = Dosen("Herman", "54321","Bahasa Inggris")

print(dsn1.perkenalan())
print(dsn2.perkenalan()) 