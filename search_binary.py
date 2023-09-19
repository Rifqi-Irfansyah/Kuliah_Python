import numpy as np

angka = np.array([2, 5, 8, 12, 16, 23, 38, 56, 72, 91])
akhir = len(angka) - 1
awal = 0

input_angka = int(input("Masukkan Angka yang Ingin Dicari Indeksnya: "))

while awal <= akhir:
    jmlh = (awal + akhir) // 2  # Membulatkan hasil pembagian menjadi bilangan bulat
    temp = angka[jmlh]

    if temp == input_angka:
        print("Angka", input_angka,"Berada Pada Indeks Ke ", jmlh)
        break
    elif temp < input_angka:
        awal = jmlh + 1
    elif temp > input_angka:
        akhir = jmlh - 1
else:
    print ("Angka", input_angka, "Tidak Ditemukan Pada Array")
