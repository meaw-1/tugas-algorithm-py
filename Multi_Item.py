import os
kode_mkn = ['a','b','c','d','e','f']
mn_mkn = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
hrg_mkn = [15000,14900,12900,13000,15000,17000]
kode_mnm = ['a','b','c','d','e']
mn_mnm = ['Teh Dingin / Hangat / Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
hrg_mnm = [2500,5000,6500,3500,5000]

print("====================")
print('   MENU MAKANAN  ')
print("====================")
for i in range(len(kode_mkn)):
	print(kode_mkn[i], mn_mkn[i], hrg_mkn[i])
	i =+ 1
print("====================")
print('   MENU MINUMAN  ')
print("====================")
for j in range(len(kode_mnm)):
	print(kode_mnm[j], mn_mnm[j], hrg_mnm[j])
	j =+ 1
ulang = 'y'
while ulang == 'y':
	print('-'*15)
	pilihan_mkn = input('MASUKKAN PILHAN MAKANAN = ')
	pilihan_mnm = input('MASUKKAN PILHAN MINUMAN = ')
	print('-'*15)
	jumlah_mkn = int(input('MASUKKAN JUMLAH MAKANAN  = '))
	jumlah_mnm = int(input('MASUKKAN JUMLAH MINUMAN  = '))

	print('-'*15)
	
	for i in range(len(mn_mkn)):
		if pilihan_mkn == kode_mkn[i] :
			harga_tot_mkn = hrg_mkn[i] * jumlah_mkn
			print('MAKANAN = ',mn_mkn[i],'   Harga = ', harga_tot_mkn)
			i =+ 1;

	for j in range(len(kode_mnm)):
		if pilihan_mnm == kode_mnm[j] :
			harga_tot_mnm = hrg_mnm[j] * jumlah_mnm
			print('MINUMAN = ', mn_mnm[j],'   Harga = ',harga_tot_mnm)
			j =+ 1;	

	ulang = input('APAKAH ANDA INGIN MEMESAN LAGI? Y/N = ')

print('-'*15)
harga_tot = harga_tot_mnm + harga_tot_mkn
print('TOTAL BELANJAAN = Rp.',harga_tot)
bayar = int(input('UANG TUNAI      = Rp. '))
bayar = bayar - harga_tot
print('KEMBALIAN       = Rp.',bayar)


