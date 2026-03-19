# Program Latihan 2.1 Operator
# Menghitung hasil dari rumus matematika:
# f(x) = (x^2 + 3x - 5) / (2x + 1)

# meminta input dari user
x = float(input("Masukkan nilai x: "))

# menghitung pembilang (atas)
pembilang = (x**2) + (3 * x) - 5

# menghitung penyebut (bawah)
penyebut = (2 * x) + 1

# menghitung hasil akhir
hasil = pembilang / penyebut

# menampilkan hasil
print("Hasil perhitungan f(x) =", hasil)