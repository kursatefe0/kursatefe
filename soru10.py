kelime= input("Bir Kelime Giriniz: ")
sesliler= "aeıioöuüAEIİOÖUÜ"

kac_sesli = 0
for harf in kelime:
 if harf in sesliler:
  kac_sesli += 1
  
print kac_sesli
