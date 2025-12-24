class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(Exception):
    """Kesalahan jika umur terlalu muda (< 5)."""
    pass

class UmurTerlaluTuaError(Exception):
    """Kesalahan jika umur lebih dari 100."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Kesalahan jika umur tidak memenuhi syarat membuat akun."""
    pass

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal 100 tahun.")
    return umur

def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun hanya untuk umur 18 tahun ke atas!")
    return "Akun berhasil dibuat."

if __name__ == "__main__":
    while True:   
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            break  # keluar loop jika tidak ada error

        except ValueError:
            print("Input harus berupa bilangan bulat!")

        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print("Error:", e)

    # Jika berhasil melewati seluruh validasi umur di atas
    print("Umur valid:", umur)

    # Coba daftar akun
    try:
        hasil = daftar_akun(umur)
        print(hasil)
    except AkunTidakDiizinkanError as e:
        print("Pendaftaran gagal:", e)
