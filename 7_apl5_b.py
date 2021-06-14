ulang = 'y'
while True :

	a = int(input("masukkan umur anda = "))
	if a >= 60 :
		status = "Lansia"
	elif a < 18 :
		status = "Remaja"
	elif a < 35 :
		status = "pemuda"
	elif a < 60 :
		status = "Dewasa"
	print(status)

	ulang = input("apakah anda ingin mengulang? y/n")