A = int(input("Cupcake fiyatı (dolar): "))
B = int(input("Cupcake fiyatı (cent): "))
N = int(input("Cupcake sayısı: "))

toplam_cent = (A * 100 + B) * N
toplam_dolar = toplam_cent // 100
kalan_cent = toplam_cent % 100

print(toplam_dolar,kalan_cent)