string = ""

bar = int(input("Masukkan angka :"))

#Looping Baris
while bar >= 0:
	kol = bar

	# Looping Kolom
	while kol > 0:
		string = string + " * "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar - 1
	
print (string)