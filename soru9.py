kelime= input("Bir Kelime Giriniz:")
harf = input("Silinecek Harfi Giriniz:")

yeni_kelime = ""

for karakter in kelime:
 if karakter != harf:
  yeni_kelime += karakter

print yeni_kelime
