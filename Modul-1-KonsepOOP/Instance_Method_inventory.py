class ManajerInventori:
    def __init__(self, pemilik, stock=0):
        self.pemilik = pemilik
        self.stock = stock

    def tambah_barang(self, jumlah):
        if jumlah > 0:
            self.stock += jumlah
            return f"Berhasil setor {jumlah}. Banyak stock: {self.stock}"
        return "Jumlah setor harus positif"

    def hapus_barang(self, jumlah):
        if 0 < jumlah <= self.stock:
            self.stock -= jumlah
            return f"Berhasil tarik {jumlah}. Banyak stock: {self.stock}"
        return "stock tidak mencukupi"

    def lihat_invetori(self):
        return f"stock {self.pemilik}: {self.stock}"

# Testing
akun = ManajerInventori("Gudang", 1000)
print(akun.tambah_barang(500))
print(akun.hapus_barang(200))
print(akun.lihat_invetori())
