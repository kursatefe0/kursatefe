sozcuk= input("Bir Sözcük Giriniz: ")
sayi= int(input("Bir Sayı Giriniz: "))
harf= input("Bir Harf Giriniz: ")

degistirilmis= sozcuk[:sayi - 1] + harf + sozcuk[sayi:]
print degistirilmis