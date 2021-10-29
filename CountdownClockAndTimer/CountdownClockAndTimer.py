import time
from plyer import notification

def notificationn(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\ahmet\\PycharmProjects\\CountdownClockAndTimer\\timer.ico",
        timeout = 10
    )

print("""
******************************
|                            |  
|      Geri Sayim Saati      |  
|            Ve              |
|        Zamanlayici         |
|                            |  
******************************
""")
try:
    t = int(input("Sayac icin saniye degeri gir: "))
except ValueError:
    print("Hata: Alfabetik karakter yerine sayi girmelisin.")
    quit()
while t:
    minutes = t // 60
    second = t % 60
    timer = "{:02d}:{:02d}".format(minutes, second)
    print("Kalan sure: ",timer,end="\r")
    time.sleep(1)
    t -= 1
notificationn("Zaman Doldu","Belirledigin sure bitti. Hoscakal !!!")
