a = int(input("jumlah pembelian printer = "))
c = 660000
b = a * c

if b > 1500000 :
	dskn = b * 0.15
	b = b - dskn
	
print("total belanjaan anda = ",b)