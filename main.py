# sekuensial
print('ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, " Beli satu botol susu, dan jika ada telor beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 175
jumlah_telur = 145
print(f"jumlah susu adalah {jumlah_botol_susu} botol")
print(f"jumlah telur adalah {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("budi tidak jadi membeli botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu") 