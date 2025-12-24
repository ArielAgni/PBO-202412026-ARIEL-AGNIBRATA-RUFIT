class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"Karyawan: {self.nama}, Gaji Pokok: {self.gaji_pokok}"


class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager: {self.nama}, Total Gaji: {total}"


class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer: {self.nama}, Total Gaji: {total}"


class Departemen:
    def __init__(self, nama_dept):
        self.nama_dept = nama_dept
        self.daftar_karyawan = []  # list of objects

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"\nDaftar Karyawan di Departemen {self.nama_dept}:")
        for k in self.daftar_karyawan:
            print(k.info_gaji())



m1 = Manager("Brori", 7000000, 2000000)
m2 = Manager("Ninang", 6500000, 1500000)

p1 = Programmer("Alip", 5000000, 1000000)
p2 = Programmer("Dranher", 5200000, 1200000)

dept = Departemen("Teknologi Informasi")

dept.tambah_karyawan(m1)
dept.tambah_karyawan(m2)
dept.tambah_karyawan(p1)
dept.tambah_karyawan(p2)

dept.tampilkan_karyawan()
