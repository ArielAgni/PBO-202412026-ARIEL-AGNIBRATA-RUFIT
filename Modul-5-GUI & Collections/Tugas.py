import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog


# ================= CLASS MAHASISWA =================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# ================= APLIKASI GUI =================
class AplikasiManajemenMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("800x500")

        # Dictionary mahasiswa
        self.data_mahasiswa = {}

        # ================= FRAME INPUT =================
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=0, column=2)
        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0)
        tk.Label(frame_input, text="IPK").grid(row=1, column=2)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, padx=5)
        self.entry_nama.grid(row=0, column=3, padx=5)
        self.entry_jurusan.grid(row=1, column=1, padx=5)
        self.entry_ipk.grid(row=1, column=3, padx=5)

        # ================= FRAME BUTTON =================
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Tambah", command=self.tambah_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Update IPK", command=self.update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Cari", command=self.cari_mahasiswa).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Filter Jurusan", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Export", command=self.export_data).pack(side=tk.LEFT, padx=5)

        # ================= TREEVIEW =================
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            frame_table,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # ================= FRAME INFO =================
        frame_info = tk.Frame(root)
        frame_info.pack(pady=5)

        tk.Button(frame_info, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_info, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)

    # ================= FUNGSI CRUD =================
    def tambah_mahasiswa(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        if not nim or not nama or not jurusan or not ipk:
            messagebox.showwarning("Error", "Semua field harus diisi")
            return

        try:
            ipk = float(ipk)
            if not (0 <= ipk <= 4):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "IPK harus angka 0 - 4")
            return

        if nim in self.data_mahasiswa:
            messagebox.showwarning("Error", "NIM sudah ada")
            return

        mhs = Mahasiswa(nim, nama, jurusan, ipk)
        self.data_mahasiswa[nim] = mhs
        self.refresh_tree()

    def hapus_mahasiswa(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")

    def update_ipk(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            ipk_baru = simpledialog.askfloat("Update IPK", "Masukkan IPK baru:")
            if ipk_baru is not None and 0 <= ipk_baru <= 4:
                self.data_mahasiswa[nim].update_ipk(ipk_baru)
                self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa")

    def cari_mahasiswa(self):
        keyword = simpledialog.askstring("Cari", "Masukkan NIM atau Nama")
        if keyword:
            hasil = [
                m for m in self.data_mahasiswa.values()
                if keyword.lower() in m.nim.lower() or keyword.lower() in m.nama.lower()
            ]
            self.tampilkan_hasil(hasil)

    def filter_jurusan(self):
        jurusan = simpledialog.askstring("Filter", "Masukkan jurusan")
        if jurusan:
            hasil = [
                m for m in self.data_mahasiswa.values()
                if jurusan.lower() == m.jurusan.lower()
            ]
            self.tampilkan_hasil(hasil)

    # ================= FITUR TAMBAHAN =================
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"{rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        m = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi", m.info())

    def export_data(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for m in self.data_mahasiswa.values():
                    f.write(m.info() + "\n")
            messagebox.showinfo("Sukses", "Data berhasil diekspor")

    # ================= UTIL =================
    def refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        for m in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))

    def tampilkan_hasil(self, hasil):
        self.tree.delete(*self.tree.get_children())
        for m in hasil:
            self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))


# ================= MAIN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenMahasiswa(root)
    root.mainloop()
