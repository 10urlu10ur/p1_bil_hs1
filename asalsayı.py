bölen= []
print("Asal sayı  ve bölen bulma programına hoş geldiniz.")
sayı = int(input("Lütfen bir pozitif tam sayı giriniz: "))
toplam= 0
for i in range(1,sayı+1):
    kalan= sayı%i
    if kalan==0:
        toplam=toplam+1
        bölen.append(i)

if toplam==2:
    print(sayı,"bir asal sayıdır, ",toplam,"böleni vardır")
else:
    print(sayı,"bir asal sayı değildir, ",toplam,"böleni vardır")
    print(bölen)