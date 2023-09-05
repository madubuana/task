# Meminta pengguna untuk memasukkan suhu dalam Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam derajat Fahrenheit: "))

# Menghitung konversi dari Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi
print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius} derajat Celsius")
