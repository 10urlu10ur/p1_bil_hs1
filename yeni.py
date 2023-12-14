# girilenSayi = int(input("Bir sayı Giriniz!"))

# carpim = 1

# for sayi in range(1, girilenSayi+1):
#     carpim *= sayi

# print(f"Girdiğin sayının faktöriyeli : {carpim}")

boylar = input("Öğrenci boylarını cm cinisinden aralarında bir boşluk bırakarak yazınız")
boydizisi = boylar.split("")
toplam = 0
for boy in boydizisi:
