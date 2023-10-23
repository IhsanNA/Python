No1 = int(input('Masukkan nomor pertama : '))
No2 = int(input('Masukkan nomor kedua : '))
tambah = No1 + No2
kurang = No1 - No2
kali = No1 * No2
bagi = No1 // No2
hasil = 'Hasil dari '

print('===================================')
print('pilih metode perhitungan')
print('- tambah')
print('- kurang')
print('- kali')
print('- bagi')
print('===================================')

opsi = str(input('Masukkan metode perhitungan : '))

if opsi == 'tambah':
    print(hasil + str(No1) + ' + ' + str(No2) + ' = ' + str(tambah))
elif opsi == 'kurang':
    print(hasil + str(No1) + ' - ' + str(No2) + ' = ' + str(kurang))
elif opsi == 'kali':
    print(hasil + str(No1) + ' x ' + str(No2) + ' = ' + str(kali))
elif opsi == 'bagi':
    print(hasil + str(No1) + ' % ' + str(No2) + ' = ' + str(bagi))
else:
    print('Maaf pilihan yang anda masukkan tidak ada')
    print('Pilih lah metode perhitungan yang ada di daftar!!')