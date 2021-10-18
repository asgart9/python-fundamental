jumlah_buku = 10

print('Ibu: "Baca semua bukumu sampai paham!"')

jumlah_buku_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0
print(f"Jumlah buku yang harus di baca {jumlah_buku}")
print(f"Jumlah buku yang sudah di baca dan dipahami {jumlah_buku_sudah_dibaca_dan_dipahami}")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_sudah_dibaca_dan_dipahami == 3:
        print(f"Buku ke {jumlah_buku_sudah_dibaca_dan_dipahami+1} belum paham")
    else:
        jumlah_buku_sudah_dibaca_dan_dipahami = jumlah_buku_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_sudah_dibaca_dan_dipahami} Sudah dibaca dan dipahami")


print(f"Jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca_dan_dipahami+1} dan yang dipahami {jumlah_buku_sudah_dibaca_dan_dipahami} buku")
if jumlah_buku_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, Tidak semua buku bisa di pahami, budi hanya paham {jumlah_buku_sudah_dibaca_dan_dipahami} buku')