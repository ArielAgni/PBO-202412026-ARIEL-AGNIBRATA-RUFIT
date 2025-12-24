import math

class Bentuk:
    def luas(self):
        return 0
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return math.pi * self.r * self.r
# Demonstrasi Polymorphism
bentuk_list = [
    Bentuk(),
    Persegi(4),
    Lingkaran(7)
]

for b in bentuk_list:
    print(f"{b.__class__.__name__} -> luas = {b.luas()}")
