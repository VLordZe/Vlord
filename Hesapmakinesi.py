print("Hesap Makinesine Hoş Geldiniz")
print(" ")

# Kullanıcıdan sayı alırken bunları float tipine dönüştürüyoruz.
sayi1 = float(input("Birinci Sayiyi Giriniz: "))
sayi2 = float(input("İkinci Sayiyi Giriniz: "))


print(" ")

print("Bir İşlem Seçiniz")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

# Kullanıcının seçimini alıyoruz.
x = input("İşleminizi Giriniz: ")

if x == "1":
    print("Sonuç: ", sayi1 + sayi2)

elif x == "2":
    print("Sonuç: ", sayi1 - sayi2)

elif x == "3":
    print("Sonuç: ", sayi1 * sayi2)

elif x == "4":
    if sayi2 != 0:
        print("Sonuç: ", sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölme işlemi yapılamaz!")

else:
    print("Seçtiğiniz İşlem Mevcut Değil")
