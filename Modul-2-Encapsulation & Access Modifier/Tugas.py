class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok
        self.__lokasi_rak = lokasi_rak

    # Getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # Setter lokasi rak
    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
        else:
            print("Stok tidak cukup!")

    def info_buku(self):
        return f"{self.judul} | Penulis: {self.penulis} | Kode: {self.kode_buku} | Stok: {self._stok} | Rak: {self.get_lokasi_rak()}"


class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali=None, status="Dipinjam"):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"Buku: {self.kode_buku} | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif=True):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam
        self.__status_aktif = status_aktif
        self.daftar_peminjaman = []  # Aggregation

    # Getter status
    def get_status(self):
        return self.__status_aktif

    # Setter status
    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, buku, tanggal_pinjam):
        if not self.__status_aktif:
            print(f"{self.nama} tidak aktif dan tidak dapat meminjam buku.")
            return
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print(f"{self.nama} sudah mencapai batas peminjaman!")
            return
        if buku._stok <= 0:
            print(f"Stok buku '{buku.judul}' habis!")
            return

        buku.kurangi_stok(1)
        peminjaman = Peminjaman(buku.kode_buku, tanggal_pinjam)
        self.daftar_peminjaman.append(peminjaman)

    def kembalikan_buku(self, kode_buku, tanggal_kembali):
        for pem in self.daftar_peminjaman:
            if pem.kode_buku == kode_buku and pem.status == "Dipinjam":
                pem.status = "Dikembalikan"
                pem.tanggal_kembali = tanggal_kembali
                return
        print("Data peminjaman tidak ditemukan!")

    def info_anggota(self):
        return f"ID: {self.id_anggota} | Nama: {self.nama} | Status Aktif: {self.get_status()}"

# Instansiasi (Demo Program)

# 3 Buku (composition di Perpustakaan -> diasumsikan dibuat di sini)
b1 = Buku("Pemrograman Python", "Guido", "B001", 3, "Rak A1")
b2 = Buku("Basis Data", "Date", "B002", 2, "Rak B1")
b3 = Buku("Jaringan Komputer", "Tanenbaum", "B003", 1, "Rak C1")

# 2 Anggota
a1 = Anggota("A01", "Ariel", 3)
a2 = Anggota("A02", "Dina", 2)

# Anggota 1 meminjam 2 buku
a1.pinjam_buku(b1, "2025-12-01")
a1.pinjam_buku(b2, "2025-12-01")

# Anggota 2 meminjam 1 buku
a2.pinjam_buku(b3, "2025-12-01")

# Pengembalian buku
a1.kembalikan_buku("B001", "2025-12-05")

delimiter = "=" * 50
print(delimiter)
print("Informasi Buku:")
print(b1.info_buku())
print(b2.info_buku())
print(b3.info_buku())

print(delimiter)
print("Informasi Anggota:")
print(a1.info_anggota())
print(a2.info_anggota())

print(delimiter)
print("Daftar Peminjaman Anggota 1:")
for p in a1.daftar_peminjaman:
    print(p.info_peminjaman())

print(delimiter)
print("Daftar Peminjaman Anggota 2:")
for p in a2.daftar_peminjaman:
    print(p.info_peminjaman())
