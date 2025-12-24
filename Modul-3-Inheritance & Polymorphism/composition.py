class Penulis:
    def __init__(self, nama):
        self.nama = nama

    def get_nama(self):
        return self.nama

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info_buku(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.get_nama()}"

penulis_novel = Penulis("Andrea Hirata")

buku_novel = Buku("Laskar Pelangi", penulis_novel)

print(f"Informasi Buku: {buku_novel.info_buku()}")
print(f"Judul: {buku_novel.judul}")
print(f"Nama Penulis (Akses Langsung): {buku_novel.penulis.nama}")