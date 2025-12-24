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


# Contoh penggunaan
if __name__ == "__main__":
    mhs = Mahasiswa("202412026", "Ariel", 3, 3.5)

    print("NIM:", mhs.nim)
    print("Nama:", mhs.nama)
    print("Semester:", mhs.get_semester())
    print("IPK:", mhs.get_ipk())

    mhs.set_semester(4)
    mhs.set_ipk(3.8)

    print("Semester (baru):", mhs.get_semester())
    print("IPK (baru):", mhs.get_ipk())
