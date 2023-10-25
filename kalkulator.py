# input var angka ke 1 dan ke 2
No1 = int(input('Masukkan angka pertama : '))
No2 = int(input('Masukkan angka kedua : '))

# var perhitungan 
tambah = No1 + No2
kurang = No1 - No2
kali = No1 * No2
bagi = No1 // No2
hasil = 'Hasil dari '

# print daftar metode perhitungan
print('===================================')
print('pilih metode perhitungan')
print('- tambah')
print('- kurang')
print('- kali')
print('- bagi')
print('===================================')

# input metode perhitungan
opsi = str(input('Masukkan metode perhitungan : '))

# pengkondisian
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
