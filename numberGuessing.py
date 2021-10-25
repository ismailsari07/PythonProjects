import random

top_of_range = input('Aklimdan tutabilecegim en buyuk sayiyi gir: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    sayi = random.randint(0, top_of_range)
    if top_of_range <=0:
        print('Lutfen bir daha kine pozitif sayi girmeyi dene.')
        quit()
else:
    print('Lutfen bir daha kine sayi girmeyi dene')
    quit()

oyundurumu = 1
print("*****Sayi Tahmin Etme Oyununa Hosgeldin*****")

while (oyundurumu == 1):
    while True:
        tahmin = input('Tahmin ettigin sayiyi gir : ')
        if tahmin.isdigit():
            tahmin = int(tahmin)
            if tahmin <= -1:
                print('Lutfen pozitif bir sayi gir')
                continue
            break
        else:
            print('Lutfen bir sayi gir: ')
            
    if (tahmin == sayi):
        print('tebrikler sayiyi buldun')
        while True:
            oyundurumu = input('\nOyuna devam etmek istermisin (1 : 0)')
            if oyundurumu != "1" and oyundurumu != "0":
                print('Lutfen 1 veya 0 degerini gir dostum (1/0): ')
                continue
            else:
                oyundurumu = int(oyundurumu)
            if (oyundurumu == 1):
                print('Aklimda yeni bir sayi tutuyorum 1 saniye.\nTamam tuttum;')
                sayi = random.randint(0, top_of_range)
            else :
                print('Tekrar gorusmek uzere dostum, kendine iyi bak.')
            break
    elif tahmin > sayi:
        print('Biraz daha asagilara dostum.')
    elif tahmin < sayi:
        print('Kafandaki sayiyi biraz daha yukselt dostum,')

