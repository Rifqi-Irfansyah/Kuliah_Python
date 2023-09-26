import numpy as np

data1 = np.array ([2, 5, 9, 19])
data2 = np.array ([1, 3, 15, 17,25])
data3 = np.concatenate((data1, data2))

# Mengurutkan
hasil_asc = np.sort(data3)
print ("data 1 ", data1)
print ("data 2 ", data2)
print ("Urutan dari Terkecil = ",hasil_asc)
print ("Urutan dari Terbesar = ",hasil_asc[::-1])