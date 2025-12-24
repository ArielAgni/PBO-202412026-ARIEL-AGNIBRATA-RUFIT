import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(
            root,
            text="Masukkan Suhu (Celsius)",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        # Entry
        self.entry_celsius = tk.Entry(root, font=("Arial", 12), width=20)
        self.entry_celsius.pack(pady=5)

        # Button Konversi
        self.button_konversi = tk.Button(
            root,
            text="Konversi ke Fahrenheit",
            command=self.konversi_suhu
        )
        self.button_konversi.pack(pady=10)

        # Label hasil
        self.label_hasil = tk.Label(
            root,
            text="Hasil: -",
            font=("Arial", 12)
        )
        self.label_hasil.pack(pady=10)

    # Fungsi konversi + validasi input
    def konversi_suhu(self):
        nilai = self.entry_celsius.get()

        # c. Validasi input
        if not nilai:
            messagebox.showwarning("Peringatan", "Masukkan nilai suhu terlebih dahulu!")
            return

        try:
            celsius = float(nilai)
            fahrenheit = (celsius * 9 / 5) + 32
            self.label_hasil.config(
                text=f"Hasil: {fahrenheit:.2f} °F"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Input harus berupa angka!"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
