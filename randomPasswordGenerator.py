import random

print("""
******************************
|       Seviye Seviye        |
|         Rastgele           |
|          Parola            |
|        Olusturucu          |
******************************   
""")

def parola_olusturma(seviye, uzunluk, adet):
    parolalar = []
    kullanilacak_karakterler = karakter_olusturma(seviye)

    for i in range(adet):
        parola = ""
        for i in range(uzunluk):
            parola += random.choice(kullanilacak_karakterler)
        parolalar.append(parola)
    return parolalar


def karakter_olusturma(seviye):
    kucuk_harfler = "abcdefghijklmnoprstuvyzqwx"
    buyuk_harfler = kucuk_harfler.upper()
    rakamlar = '1234567890'
    nispeten_cok_kullanilan_isaretler = ",.?;'(!#%=-)"
    tum_isaretler = "`[]-=\;'/.\",~!@#$%^&*()_+}{|:?><"

    if seviye == 1:
        return kucuk_harfler + rakamlar
    elif seviye == 2:
        return buyuk_harfler + kucuk_harfler + rakamlar
    elif seviye == 3:
        return buyuk_harfler + kucuk_harfler + rakamlar + nispeten_cok_kullanilan_isaretler
    elif seviye == 4:
        return buyuk_harfler + kucuk_harfler + rakamlar + tum_isaretler


print("""
1. Dusuk guvenlikli parola: Sadece kucuk harf ve sayilardan olusturur.
2. Orta guvenlikli parola: Buyuk harf, kucuk harf ve sayilardan olusturur.
3. Orta-Yuksek guvenlikli parola: Buyuk harf, kucuk harf, sayi ve nispeten cok kullanilan isaretlerden olusturur.
4. Yuksek guvenlikli parola: Klavyede kullanilabilecek butun karakterleden olusturur (Buyuk harf, kucuk harf, sayi ve tum isaretler).
""")
try:
    seviye = int(input("Guvenlik seviyesini gir: "))
    uzunluk = int(input("Parolanin uzunlugunu gir: "))
    adet = int(input("Kac adet parola olusturulsun? "))
except ValueError:
    print("Hata: Pozitif sayidan baska bir karakter girdiniz.")
    quit()

parolalar = parola_olusturma(seviye,uzunluk,adet)
print("\n")
for index, parola in enumerate(parolalar):
    print(f"{index}. parola = {parola}")
print("\nGuclu parola, guclu guvenlik.")