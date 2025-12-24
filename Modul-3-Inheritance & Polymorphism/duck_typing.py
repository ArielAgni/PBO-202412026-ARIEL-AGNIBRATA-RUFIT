class Laptop:
    def nyalakan(self):
        return "Laptop menyala: sistem operasi booting..."

class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala: layar utama aktif."

def tes_nyala(obj):
    print(obj.nyalakan())

# Duck typing dalam aksi
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)