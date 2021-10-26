def sayiMi(stringTipindeSayi):
    if stringTipindeSayi.isdigit():
        stringTipindeSayi = int(stringTipindeSayi)
        if stringTipindeSayi <= 0:
            print("Lutfen bir daha ki sefere 0'dan buyuk sayi girmeyi dene.")
            quit()
    else: 
        print("Bir daha ki sefere sayi girmeyi dene.")
        quit()
    return stringTipindeSayi

kisiAdet = input("Kac kisi kaydetmek istiyorsun: ")
kisiAdet = sayiMi(kisiAdet)
name = []
surname = []
email = []
phone = []

for i in range(kisiAdet):
    name.append(input("Enter Name : ")) 
    surname.append(input("Enter Surname : "))
    email.append(input("Enter Email : "))
    phone.append(input("Enter Phone : "))

print("\n\nKaydediliyor...\r\t\t\t\t\tTamamlandi")
print('Listeleniyor...\r\t\t\t\t\tTamamlandi\n\n')

print("Name\r\t\tSurname\r\t\t\t\t\tEmail\r\t\t\t\t\t\t\t\t\tPhone")

for i in range(kisiAdet):
    print("{}\r\t\t{}\r\t\t\t\t\t{}\r\t\t\t\t\t\t\t\t\t{}".format(name[i],surname[i],email[i],phone[i]))    




