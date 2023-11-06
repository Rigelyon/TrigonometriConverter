import numpy as np
import matplotlib.pyplot as plt
import os
import math


class ProgramFungsi:
    def __init__(self):
        pass

    # Fungsi Trigonometri
    def fungsi_trigonometri(self, x, tipe) -> float:
        if tipe == "sin":
            return math.sin(x)
        if tipe == "cos":
            return math.cos(x)
        if tipe == "tan":
            return math.tan(x)
        if tipe == "cosecan":
            cosecan = 1 / math.sin(x)
            return cosecan
        if tipe == "secan":
            secan = 1 / math.cos(x)
            return secan
        if tipe == "cotangen":
            cotangen = 1 / math.tan(x)
            return cotangen
        else:
            return "Tulis tipe Trigonometri dengan benar!"

    # # Fungsi Linear
    # def fungsi_linear_x(self, y, a, b) -> float:
    #     x = (y / a) - (b / a)
    #     return x

    # def fungsi_linear_y(self, x, a, b) -> float:
    #     y = a * x + b
    #     return y

    # # Fungsi Kuadrat
    # def fungsi_kuadrat_x(self, y, a, b, c) -> float:
    #     xa = -(b + math.sqrt(b**4 - a * c + 4 * a * y) / 2 * a)
    #     xb = -(b - math.sqrt(b**4 - a * c + 4 * a * y) / 2 * a)
    #     return xa, xb

    # def fungsi_kuadrat_y(self, x, a, b, c) -> float:
    #     y = ((a * x) ** 2) + (b * x) + c
    #     return y

    # def fungsi_kuadrat_puncak_absis(self, a, b) -> float:
    #     Absis = -(b / 2 * a)
    #     return Absis

    # def fungsi_kuadrat_puncak_ordinat(self, a, D) -> float:
    #     Ordinat = -(D / 4 * a)
    #     return Ordinat

    # # Funsgi Kubik
    # # To do implement
    # def fungsi_kubik_y(self, x, a, b, c, d) -> float:
    #     y = ((a * x) ** 3) + ((b * x) ** 2) + (c * x) + d
    #     return y

    # def fungsi_kubik_x(self, y, a, b, c, d) -> float:
    #     pass

    # # Fungsi Logaritma
    # def fungsi_logaritma(self, x, base) -> float:
    #     if x <= 0:
    #         return "Invalid input untuk Logaritma"
    #     return math.log(x, base)

    # # Fungsi Eksponensial
    # def fungsi_eksponensial(self, x, y):
    #     pass

    # def plot_graph(self, x, y, a, b, c, d):
    #     x_axes = np.arange(10 - x, 10 + x)
    #     pass

    # def pilih_operasi(self):
    #     os.system("cls")
    #     print("OPERASI FUNGSI KUADRAT")
    #     print("======================")
    #     print("\n1.| Fungsi Linear (y = mx + b)")
    #     print("2.| Fungsi Kuadrat (y = ax^2 + bx + c)")
    #     print("3.| Fungsi Kubik (y = ax^3 + bx^2 + cx + d)")
    #     print("4.| Fungsi Trigonometri")
    #     print("5.| Fungsi Logaritma")
    #     print("6.| Fungsi Eksponensial (y = ax)")
    #     choice = input("\nPilih Operasi (1/2/3/4/5/6): ")

    #     if choice == "1":
    #         print("===== FUNGSI LINEAR =====")
    #         print("y = ax + b\n")
    #         a = float(input("Masukkan gradien (a): "))
    #         b = float(input("Masukkan intercept-y (b): "))
    #         xy_choice = str(input("Pilih yang ingin dicari (X atau Y): "))
    #         if xy_choice.lower == "x":
    #             y = float(input("\nMasukkan nilai Y: "))
    #             x = self.fungsi_linear_x(y, a, b)
    #         else:
    #             x = float(input("\nMasukkan nilai X: "))
    #             y = self.fungsi_linear_y(x, a, b)

    #         print("Hasil operasi Fungsi Linear: y = ax + b =", int(y))
    #         print(f"\nDengan titik: [{int(x)},{int(y)}]")
    #     else:
    #         print("Bukan pilihan yang benar")
    #         return

    # def mulai_fungsi(self):
    #     while True:
    #         self.pilih_operasi()
    #         repeater = str(input("Apakah ingin mengulang operasi(Yes/no)? "))
    #         if repeater.lower() != "yes":
    #             break


if __name__ == "__main__":
    Fungsi = ProgramFungsi()
    Fungsi.mulai_fungsi()
