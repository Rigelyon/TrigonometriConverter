import numpy as np
import matplotlib.pyplot as plt
import os
import math

# import seaborn as sns


class ProgramFungsi:
    def __init__(self):
        pass

    def pilih_operasi(self):
        os.system("cls")
        print("OPERASI FUNGSI KUADRAT")
        print("======================")
        print("\n1.| Fungsi Linear (y = mx + b)")
        print("2.| Fungsi Kuadrat (y = ax^2 + bx + c)")
        print("3.| Fungsi Kubik (y = ax^3 + bx^2 + cx + d)")
        print("4.| Fungsi Trigonometri")
        print("5.| Fungsi Logaritma")
        choice = input("\nPilih Operasi: ")

        linear = FungsiLinear()
        if choice == "1":
            print("===== FUNGSI LINEAR =====")
            print("y = ax + b\n")
            a = float(input("Masukkan gradien (a): "))
            b = float(input("Masukkan intercept-y (b): "))
            xy_choice = str(input("Pilih yang ingin dicari (X atau Y): "))
            if xy_choice.lower == "x":
                y = float(input("Masukkan nilai Y: "))
                x = linear.fungsi_linear_x(x, a, b)
            else:
                x = float(input("Masukkan nilai X: "))
                y = linear.fungsi_linear_y(y, a, b)
        else:
            print("Bukan pilihan yang benar")
            return

        print("Hasil operasi Fungsi Linear: y = ax + b =", int(y))
        print(f"Dengan titik: [{int(x)},{int(y)}]")

    def mulai_fungsi(self):
        while True:
            self.pilih_operasi()
            repeater = str(input("Apakah ingin mengulang operasi(Yes/no)? "))
            if repeater.lower() != "yes":
                break


class FungsiLinear(ProgramFungsi):
    def __init__(self):
        pass

    def fungsi_linear_x(self, y, a, b):
        return (y / a) - (b / a)

    def fungsi_linear_y(self, x, a, b):
        return a * x + b


class FungsiEksponen:
    def __init__(self):
        pass


class FungsiKuadrat:
    def __init__(self):
        pass

    def fungsi_kuadrat_x(self, y, a, b, c):
        xa = -(b + math.sqrt(b**4 - a * c + 4 * a * y) / 2 * a)
        xb = -(b - math.sqrt(b**4 - a * c + 4 * a * y) / 2 * a)
        return xa, xb

    def fungsi_kuadrat_y(self, x, a, b, c):
        return ((a * x) ** 2) + (b * x) + c

    def fungsi_kuadrat_puncak_absis(self, a, b):
        Absis = -(b / 2 * a)
        return Absis

    def fungsi_kuadrat_puncak_ordinat(self, a, D):
        Ordinat = -(D / 4 * a)
        return Ordinat


class FungsiKubik:
    def __init__(self):
        pass

    def fungsi_kubik(self, x, a, b, c, d):
        return ((a * x) ** 3) + ((b * x) ** 2) + (c * x) + d


class FungsiTrigonometri:
    def __init__(self):
        pass

    def fungsi_trigonometri(self, x, tipe):
        if tipe == "sin":
            return math.sin(x)
        if tipe == "cos":
            return math.cos(x)
        if tipe == "tan":
            return math.tan(x)
        else:
            return "Tulis tipe Trigonometri dengan benar!"


class FungsiLogaritma:
    def __init__(self):
        pass

    def fungsi_logaritma(self, x, base):
        if x <= 0:
            return "Invalid input untuk Logaritma"
        return math.log(x, base)


if __name__ == "__main__":
    Fungsi = ProgramFungsi()
    Fungsi.mulai_fungsi()
