import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import os
import math

class ProgramFungsi:
    def __init__(self):
        pass

    def fungsiLinear(self, x, a, b):
        return a * x + b
    
    def fungsiKuadrat(self, x, a, b, c):
        return ((a * x)**2) + (b * x) + c

    def fungsiKubik(self, x, a, b, c, d):
        return ((a * x)**3) + ((b * x)**2) + (c * x) + d

    def fungsiTrigonometri(self, x, tipe):
        if tipe == "sin":
            return math.sin(x) 
        if tipe == "cos":
            return math.cos(x)
        if tipe == "tan": 
            return math.tan(x)
        else:
            return "Tulis tipe Trigonometri dengan benar!"

    def fungsiLogaritma(self, x, base):
        if x <= 0:
            return "Invalid input untuk Logaritma"
        return math.log(x, base)
    
    def pilihOperasi(self):
        os.system("cls")
        print("OPERASI FUNGSI KUADRAT")
        print("======================")
        print("\n1.| Fungsi Linear (ax + b)")
        print("2.| Fungsi Kuadrat (ax^2 + bx + c)")
        print("3.| Fungsi Kubik (ax^3 + bx^2 + cx + d)")
        print("4.| Fungsi Trigonometri")
        print("5.| Fungsi Logaritma")
        choice = input("\nPilih Operasi: ")

        if choice == "1":
            print("===== FUNGSI LINEAR =====")
            print("ax + b\n")
            x = float(input("Masukkan nilai x: "))
            a = float(input("Masukkan gradien (a): "))
            b = float(input("Masukkan intercept-y (b): "))
            hasil = self.fungsiLinear(x, a, b)
        else:
            print("Bukan pilihan yang benar")
            return
        
        print("Hasil operasi: ", hasil)

    def mulaiFungsi(self):
        while(True):
            self.pilihOperasi()
            repeater = str(input("Apakah ingin mengulang operasi(Yes/no)? "))
            if repeater.lower() != "yes":
                break
if __name__ == "__main__":
    Fungsi = ProgramFungsi()
    Fungsi.mulaiFungsi()