class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"

data_pelanggan = {
    "C001": Pelanggan("C001", "Jamal", "Jamal@email.com"),
    "C002": Pelanggan("C002", "Nura", "Nura@email.com")
}

def tambah_pelanggan(data, pelanggan):
    data[pelanggan.id_pelanggan] = pelanggan
    print("Pelanggan berhasil ditambahkan")


# Fungsi untuk menghapus pelanggan
def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]
        print("Pelanggan berhasil dihapus")
    else:
        print("Pelanggan tidak ditemukan")


# Fungsi untuk mencari pelanggan
def cari_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        return data[id_pelanggan]
    return None

def tampilkan_semua_pelanggan(data):
    print("\n=== Daftar Pelanggan ===")
    if not data:
        print("Data pelanggan kosong")
    for pelanggan in data.values():
        print(pelanggan.info())


# ===== Contoh penggunaan =====
tampilkan_semua_pelanggan(data_pelanggan)

pelanggan_baru = Pelanggan("C003", "Budi", "budi@email.com")
tambah_pelanggan(data_pelanggan, pelanggan_baru)

tampilkan_semua_pelanggan(data_pelanggan)

hasil = cari_pelanggan(data_pelanggan, "C002")
if hasil:
    print("\nPelanggan ditemukan:", hasil.info())
else:
    print("\nPelanggan tidak ditemukan")

hapus_pelanggan(data_pelanggan, "C001")

tampilkan_semua_pelanggan(data_pelanggan)
