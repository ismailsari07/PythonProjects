print("""
******************************
|            Dort            |
|           Islemli          |
|      Hesap Makinesi'ne     |
|         Hosgeldiniz        |
******************************
""")

while True:
    try:
        number1 = int(input("Birinci sayiyi gir: "))
        number2 = int(input("Ikinci sayiyi gir: "))
        islem = int(input("""1. Toplama\n2. Cikarma\n3. Carpma\n4. Bolme\nYapacagin islemin numarasini gir (Cikmak icin 0 gir): """))
    except ValueError:
        print("Lutfen alfabetik karakter yerine sayi girin.")
        continue
    if islem == 1:
        print(f"{number1} + {number2} = {number1 + number2}")
    elif islem == 2:
        print(f"{number1} - {number2} = {number1 - number2}")
    elif islem == 3:
        print(f"{number1} * {number2} = {number1 * number2}")
    elif islem == 4:
        if number2 == 0:
            print("Matematikte sayilar 0'a bolunemez.")
        else:
            print(f"{number1} / {number2} = {number1 / number2}")
    elif islem == 0:
        print("Hesap makinesinden cikiliyor.")
        break
    else:
        print("Lutfen belirtilen sayilardan birini girmeyi dene.")

