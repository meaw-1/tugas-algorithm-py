ulang = 'y'
while True :
	a = int(input ("masukkan nilai = "))

	if a > 60 :
		status = "LULUS"
	elif a <= 60 :
		status = "TIDAK LULUS"
	print(status)

	ulang = input("apakah anda ingin mengulang? y/n = ")