daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
print('Tampilkan Variabel daftar_buku')
print(daftar_buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Vol 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku.append('ReactJS E-Commerce')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku[0] = 'Django Dev'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-3')
buku = daftar_buku.pop(2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

