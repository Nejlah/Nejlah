#membuat contoh dictionary
biodata = {
    'nama': 'nejlah',
    'usia': 18,
    'asal': 'kediri'
    }
#menampilkan dictionary dengan perulangan
for i in biodata.items ():
    print(i)

for i in biodata:
    print(i)

for i in biodata.values ():
    print(i)

#mengupdate salah satu dictionary
biodata ['usia'] = 19
print(biodata)

#mengahpus salah satu dictionary
biodata.pop('asal')
print(biodata)

print(biodata.popitem())

biodata.clear ()
print(biodata)

#del biodata
#print(biodata)

#menambahkan dictionary
biodata['daftar'] = 'mahasiswa'
print(biodata)
