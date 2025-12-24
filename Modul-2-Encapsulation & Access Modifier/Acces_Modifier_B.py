class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim                # public
        self.nama = nama              # public
        self._semester = semester     # protected
        self.__ipk = ipk              # private

    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected
    def set_semester(self, sem_baru):
        if sem_baru <= 0:
            raise ValueError("Semester harus lebih dari 0.")
        self._semester = sem_baru

    # Getter private
    def get_ipk(self):
        return self.__ipk

    # Setter private
    def set_ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError("IPK harus di antara 0.0 - 4.0.")
        self.__ipk = nilai

    def naik_semester(self):
        self._semester += 1
        return self._semester



if __name__ == "__main__":
    
    mhs1 = Mahasiswa("202412026", "Ariel", 1, 4.0)

    
    mhs2 = Mahasiswa("202412055", "Herman", 2, 3.5)

    print("=== Data Mahasiswa 1 ===")
    print("NIM:", mhs1.nim)
    print("Nama:", mhs1.nama)
    print("Semester:", mhs1.get_semester())
    print("IPK:", mhs1.get_ipk())

    print("\n=== Data Mahasiswa 2 ===")
    print("NIM:", mhs2.nim)
    print("Nama:", mhs2.nama)
    print("Semester:", mhs2.get_semester())
    print("IPK:", mhs2.get_ipk())
