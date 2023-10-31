#1. [kodeKendaraan, namaKendaraan, ccKendaraan, warnaKendaraan]
kendaraan = ['B 1234 ZZZ', 'Supra X', 125, 'Hitam']
print(kendaraan)

#2. diakhir tambahkan [harga kendaraan dan jumlah roda],
#   disisipkan setelah nama kendaraan [merk kendaraan dan jenis kendaraan]
kendaraan.append(23_000_000)
kendaraan.append(2)
print(kendaraan)

kendaraan.insert(2, 'Honda')
kendaraan.insert(3, 'Motor')
print(kendaraan)

#3. Buat program bahasa python dengan match case untuk menghitung luas bangun datar
#   1. luas persegi
#   2. luas lingkaran
#   3. luas segitiga
#   selain itu beri keterangan salah

print("""
Selamat datang di program menghitung luas
    Menu
    1. Menghitung luas persegi
    2. Menghitung luas lingkaran
    3. Menghitung luas segitiga
""")

pilihan = input('Silahkan pilih, 1 / 2 / 3:\n')

match pilihan:
    case '1':
        sisi_persegi = int(input('Silahkan masukkan sisi persegi:\n'))
        luas_persegi = sisi_persegi * sisi_persegi
        print('Luas persegi dari sisi ' + str(sisi_persegi) + ' adalah ' + str(luas_persegi))
    case '2':
        jari_jari = int(input('Silahkan masukkan jari-jari lingkaran:\n'))
        luas_lingkaran = 22/7 * jari_jari ** 2
        print('Luas lingkaran dengan jari-jari', jari_jari, 'adalah', luas_lingkaran)
    case '3':
        alas = int(input('Silahkan masukkan alas segitiga:\n'))
        tinggi = int(input('Silahkan masukkan tinggi segitiga:\n'))
        luas_segitiga = alas * tinggi / 2
        print('Luas lingkaran dengan alas', alas, 'dan tinggi', tinggi, 'adalah', luas_segitiga)
    case _:
        print('Tidak ada dalam pilihan')

