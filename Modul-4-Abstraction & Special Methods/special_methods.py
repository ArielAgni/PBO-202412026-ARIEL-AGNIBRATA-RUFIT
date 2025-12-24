class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)

    def __eq__(self, other):
        return self.nilai == other.nilai

m1 = Mahasiswa("Pouster", 80)
m2 = Mahasiswa("Ahmad", 90)
m3 = Mahasiswa("Budi", 80)


print(m1)
print(m2)
print(m3)


print("Apakah m1 == m3 ?", m1 == m3)   
print("Apakah m1 == m2 ?", m1 == m2)   


print("m1 + m2 =", m1 + m2)
print("m2 * 2 =", m2 * 2)


print("Panjang nama m1 =", len(m1))
print("Panjang nama m2 =", len(m2))


daftar = [m1, m2, m3]
urut = sorted(daftar, key=lambda x: x.nilai)

print("\nHasil sorting berdasarkan nilai:")
for m in urut:
    print(m)
