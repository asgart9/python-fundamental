# Sekuensial
print('Ibu berkata: "Pergi ke toko"')
print('Budi Menjawab: "Baik, Apa yang hasrus saya lakukan di toko?"')
print('Ibu Menjawab: "Beli satu botol susu, dan jika ada telur beli 6')
print("Budi Berangkat Ke toko")
print("Budi mulai berbelanja")

# Percabangan
jumlah_botol_susu = 70

jumlah_telur = 100

print("Budi memerikasa ketersediaan Susu")
if jumlah_botol_susu > 0:
    print(f">> Susu Tersedia {jumlah_botol_susu} botol")
    print("Budi memerikasa ketersediaan Telur")
    if jumlah_telur == 0:
        print(">> Telur Tidak Tersedia")
        print("Budi Tidak Membeli Telur")
    else:
        print(f">> Telur Tersedia {jumlah_telur} Butir")
        print("Budi membeli 6 Butir susu")
    print("Budi Membeli 1 Botol Susu")
else:
    print(">> Susu Tidak Tersedia")
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi Kembali kerumah")
print("Memberikan hasilnya kepada ibu")
