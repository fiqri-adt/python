"""
Program perulangan membaca buku dgn While
"""

jumlah_buku = 20
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} ')

while jumlah_buku_yang_sudah_dibaca_dan_dipahami < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca ")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami} ')
