import random
sayi = random.randint(0, 10)
oyundurumu = 1
print("*****Sayi Tahmin Etme Oyununa Hosgeldin*****")
while (oyundurumu == 1):
    tahmin = int(input('Tahmin ettigin sayiyi gir : '))
    if (tahmin == sayi):
        oyundurumu = int(input('Tebrikler sayiyi buldun\nOyuna devam etmek istermisin (1 : 0)'))
        if (oyundurumu == 1):
            print('Aklimda yeni bir sayi tutuyorum 1 saniye.\nTamam tuttum;')
            sayi = random.randint(0, 10)
        else :
            print('Tekrar gorusmek uzere dostum, kendine iyi bak.')
    elif tahmin > sayi:
        print('Biraz daha asagilara dostum.')
    elif tahmin < sayi:
        print('Kafandaki sayiyi biraz daha yukselt dostum,')

