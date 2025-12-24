import tkinter as tk
from tkinter import messagebox

class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi GUI Sederhana")
        self.root.geometry("300x220")

        # a. Label
        self.label = tk.Label(
            root,
            text="Masukkan Nama Anda",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        # a. Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # a & b. Button untuk menampilkan isi Entry
        self.button_sapa = tk.Button(
            root,
            text="Tampilkan",
            command=self.tampilkan_isi
        )
        self.button_sapa.pack(pady=5)

        self.button_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus_isi
        )
        self.button_hapus.pack(pady=5)

    def tampilkan_isi(self):
        isi = self.entry.get()
        if isi:
            messagebox.showinfo("Isi Entry", f"Isi Entry: {isi}")
        else:
            messagebox.showwarning("Peringatan", "Entry masih kosong!")

    def hapus_isi(self):
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Info", "Isi Entry berhasil dihapus")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
