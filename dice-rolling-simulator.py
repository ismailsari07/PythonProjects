import random
print('*****Zar Atma Oyununa Hosgeldiniz*****')
oyundurumu = 1;
while (oyundurumu == 1):
    zarNumber = random.randint(1,6)
    print('Zar ', zarNumber, "'i gosteriyor")
    oyundurumu = int(input('Oyuna devam etmek istiyormusun (1 : 0) = '))
    if oyundurumu == 0:
        print("Tekrar gorusmek uzere dostum kendine iyi bak.")
    else :
        print('Zar atiliyor.')
