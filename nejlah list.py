#membuat contoh list
hewan = ["ayam","sapi","buaya","kucing","cicak"]

#menampilkan list dengan perulangan
for i in hewan:
    print(i)

i = 0
while i < len(hewan):
    print(hewan[i])
    i += 1

#mengupdate salah satu list
hewan [2] = "ular"
print(hewan)

#menghapus salah satu list
hewan.pop ()
print(hewan)

del hewan [1:3]
print(hewan)

hewan.remove("ayam")
print(hewan)

#menambahkan list
hewan.append("ayam")
print(hewan)

hewan.extend (["sapi","angsa"])
print(hewan)

hewan.insert(2,"burung")
print(hewan)
