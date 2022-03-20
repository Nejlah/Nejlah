#membuat contoh tuple
benda = ("buku","pensil","sapu","kursi","meja")

#menampilkan tuple dengan perulangan
for i in benda:
    print(i)

b = 0
while b < len(benda):
    print(benda[b])
    b += 1

benda = list(benda)
#mengupdate salah satu tuple
benda [2] = "gelas"
print(benda)

#menghapus salah satu tuple
benda.pop ()
print(benda)

benda.remove ("pensil")
print(benda)

del benda [0:2]
print(benda)

#menambahkan tuple
benda.append ("sendok")
print(benda)

benda.extend (["pisau","garpu"])
print(benda)

benda.insert(2,"piring")
print(benda)
