daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
print('Tampilkan Variabel daftar_buku')
print(daftar_buku)

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
del daftar_buku[:] #Start:Stop
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
del daftar_buku[0:1] #Start:End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
del daftar_buku[0:-2] #Start:End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
del daftar_buku[0::2] #Start:End:Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku_baru = daftar_buku[0::2] #ganjil
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku_baru = daftar_buku[1::2] #genap
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang bagian diujung')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
daftar_buku_baru = daftar_buku[0:-1] 
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

#Cara Simple
print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['Habibie & Ainun', 'Solat Tahadjud', 'Flutter Course']
print(daftar_buku[0:1])
