if __name__ == '__main__':
    number = input("Hangi sayinin fibonacci dizisinde olup olmadigini kontrol etmek istiyorsun: ")
    if number.isdigit():
        number = int(number)
        if number < 0:
            print("Lutfen bir daha ki sefere pozitif sayi girmeyi dene.")
            quit()
    else:
        print("Lutfen bir daha ki sefere alfabetik karakter yerine sayi girmeyi dene")
        quit()

    a = 0
    b = 1
    while True:
        c = a + b
        if number == c or number == a:
            print(f"{number} fibonacci sayidir")
            break
        elif number < c:
            print(f"{number} fibonacci sayisi degildir")
            break
        a = b
        b = c


