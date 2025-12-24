import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


# b. Class Tugas
class Tugas:
    def __init__(self, judul, status="Belum Selesai"):
        self.judul = judul
        self.status = status


# a. Aplikasi GUI Manajemen Tugas
class AplikasiManajemenTugas:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas")
        self.root.geometry("600x400")

        # b. List of objects
        self.daftar_tugas = []

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul Tugas:").grid(row=0, column=0)
        self.entry_judul = tk.Entry(frame_input, width=30)
        self.entry_judul.grid(row=0, column=1, padx=5)

        tk.Button(
            frame_input,
            text="Tambah Tugas",
            command=self.tambah_tugas
        ).grid(row=0, column=2, padx=5)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai)\
            .pack(side=tk.LEFT, padx=5)

        # ===== Frame Tabel =====
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Judul", "Status"),
            show="headings"
        )
        self.tree.heading("Judul", text="Judul Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

    # c. Tambah tugas
    def tambah_tugas(self):
        judul = self.entry_judul.get()
        if judul:
            tugas = Tugas(judul)
            self.daftar_tugas.append(tugas)

            self.tree.insert("", tk.END, values=(judul, tugas.status))
            self.entry_judul.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Judul tugas tidak boleh kosong!")

    # c. Hapus tugas
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.tree.delete(selected[0])
            del self.daftar_tugas[index]
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

    # c. Edit tugas
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            judul_baru = simpledialog.askstring(
                "Edit Tugas",
                "Masukkan judul baru:",
                initialvalue=tugas.judul
            )

            if judul_baru:
                tugas.judul = judul_baru
                self.tree.item(
                    selected[0],
                    values=(tugas.judul, tugas.status)
                )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang ingin diedit!")

    # c. Tandai selesai
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            tugas.status = "Selesai"
            self.tree.item(
                selected[0],
                values=(tugas.judul, tugas.status)
            )
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenTugas(root)
    root.mainloop()
