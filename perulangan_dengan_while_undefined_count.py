book_count = 10

print('Ibu: "Baca semua bukumu sampai paham!"')

understood_count = 0
read_count = 0
print(f"Jumlah buku yang harus di baca {book_count}")
print(f"Jumlah buku yang sudah di baca dan dipahami {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 3:
        print(f"Buku ke {understood_count + 1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} Sudah dibaca dan dipahami")


print(f"Jumlah buku yang sudah dibaca {understood_count + 1} dan yang dipahami {understood_count} buku")
if understood_count == book_count:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, Tidak semua buku bisa di pahami, budi hanya paham {understood_count} buku')
