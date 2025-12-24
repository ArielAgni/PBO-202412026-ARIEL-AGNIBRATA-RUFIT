from abc import ABC, abstractmethod

# ==========================
# 1. ABSTRACT CLASS
# ==========================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# ==========================
# 4. CUSTOM EXCEPTION
# ==========================
class PoinTidakValidError(Exception):
    def __init__(self, pesan="Poin tidak boleh bernilai negatif!"):
        super().__init__(pesan)


# ==========================
# 2. CHILD CLASS + SPECIAL METHODS
# ==========================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        return f"{self.nama} memiliki akses sebagai Member."

    # __str__()
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    # __add__()
    def __add__(self, other):
        return self.poin + other.poin

    # __len__()
    def __len__(self):
        return len(self.nama)


# ==========================
# 3 & 4. EXCEPTION HANDLING + CUSTOM EXCEPTION
# ==========================
def input_poin():
    try:
        user_input = input("Masukkan poin member: ")

        if user_input.strip() == "":
            raise ValueError("Input tidak boleh kosong!")

        poin = float(user_input)

        if poin < 0:
            raise PoinTidakValidError()

        return poin

    except ValueError as e:
        print(f"Kesalahan input: {e}")
    except PoinTidakValidError as e:
        print(f"Error custom: {e}")


# ==========================
# PROGRAM UTAMA
# ==========================
if __name__ == "__main__":

    print("=== Input Poin ===")
    p1 = input_poin()    
    p2 = input_poin()

    if p1 is None: p1 = 0
    if p2 is None: p2 = 0

    
    m1 = Member("Abrar", p1)
    m2 = Member("Topik", p2)

    print("\n=== Info Member ===")
    print(m1)
    print(m2)

    print("\n=== Hak Akses ===")
    print(m1.akses())

    print("\n=== Operasi Special Methods ===")
    print("Jumlah poin (m1 + m2):", m1 + m2)
    print("Panjang nama m1:", len(m1))

    print("\n=== Uji Exception: Masukkan poin negatif ===")
    input_poin()   
