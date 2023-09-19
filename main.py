panjang = int (input("Masukkan Panjang: "))
lebar   = int (input("Masukkan Lebar: "))
luas    = panjang * lebar

print ("Luas: ", luas)
if luas < 50:
    print ("Tanah saya")
else :
    print ("Tanah orang lain")
    
print ("Lokasi Memori dalam decimal : ", id(luas))
print ("Lokasi Memori dalam hex     : ", hex(id(luas)))