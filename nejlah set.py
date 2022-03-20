#membuat contoh set
nama = {"ella", 10, False, 5, "ipa"}

#menampilkan set dengan perulangan
for i in nama :
    print(i)

nama = list(nama)
i = 0
while i < len(nama):
    print(nama[i])
    i += 1 

#mengupdate salah satu set
nama [1] = "bantal"
print(nama)

nama = set(nama)
#menghapus salah satu set
nama.remove ("bantal")
print(nama)

nama.discard (5)
print(nama)

nama.pop ()
print(nama)

nama.clear ()
print(nama)

#menambahkan set
nama.add ("ella")
print(nama)

nama.update (["baju","bedak"])
print(nama)
