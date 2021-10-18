jumlah_buku = 10

print('Ibu: "Baca semua bukumu sampai paham!"')

Jumlah_baca_paham = 0
jumlah_baca = 0
print(f"Jumlah buku yang harus di baca {jumlah_buku}")
print(f"Jumlah buku yang sudah di baca dan dipahami {Jumlah_baca_paham}")

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if Jumlah_baca_paham == 3:
        print(f"Buku ke {Jumlah_baca_paham + 1} belum paham")
    else:
        Jumlah_baca_paham = Jumlah_baca_paham + 1
        print(f"Buku ke {Jumlah_baca_paham} Sudah dibaca dan dipahami")


print(f"Jumlah buku yang sudah dibaca {Jumlah_baca_paham + 1} dan yang dipahami {Jumlah_baca_paham} buku")
if Jumlah_baca_paham == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, Tidak semua buku bisa di pahami, budi hanya paham {Jumlah_baca_paham} buku')
