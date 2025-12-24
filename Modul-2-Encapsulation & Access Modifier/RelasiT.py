class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # (f) method rata_rata()
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# Composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# Fungsi report
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"\n=== Program Studi: {prodi.nama} ===")
    print("Daftar Mata Kuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa & Rata-rata Nilai:")

    for m in semua_mahasiswa:
        relevan = [
            n for n in m.daftar_nilai
            if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)
        ]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg, 2)}")
    print("--------------------------------------")

if __name__ == "__main__":

    # (a) Tambahkan 2 Program Studi
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")

    # (b) Tambahkan minimal 2 mata kuliah untuk masing-masing prodi
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Sistem Informasi Manajemen"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Analisis Sistem"))

    # (c) Buat 3 Mahasiswa + objek Nilai (DATA SUDAH DIGANTI)
    m1 = Mahasiswa("202412065", "Abror")
    m2 = Mahasiswa("202412089", "Yere")
    m3 = Mahasiswa("202412076", "Karel")

    # Tambahkan nilai
    m1.tambah_nilai(Nilai("TI101", 80))
    m1.tambah_nilai(Nilai("TI102", 75))
    m1.tambah_nilai(Nilai("SI201", 70))

    m2.tambah_nilai(Nilai("TI101", 90))
    m2.tambah_nilai(Nilai("SI202", 88))

    m3.tambah_nilai(Nilai("SI201", 78))
    m3.tambah_nilai(Nilai("SI202", 82))

    semua_mahasiswa = [m1, m2, m3]

    # (d) Tampilkan daftar mata kuliah tiap prodi
    print("=== Daftar Mata Kuliah Setiap Prodi ===")
    for p in uni.programs:
        print(f"{p.nama}: {[mk.kode for mk in p.daftar_matakuliah]}")

    # (e) Tampilkan daftar nilai setiap mahasiswa
    print("\n=== Daftar Nilai Mahasiswa ===")
    for m in semua_mahasiswa:
        print(f"{m.nim} - {m.nama}:")
        for n in m.daftar_nilai:
            print(f"   {n.kode_mk} = {n.skor}")
        print(f"   Rata-rata: {round(m.rata_rata(), 2)}")  # (f)

    # (g) Panggil fungsi report_program untuk setiap prodi
    for p in uni.programs:
        report_program(p, semua_mahasiswa)
