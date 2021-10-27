from plyer import notification
import time
def notificationn(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\ahmet\\PycharmProjects\\desktopNotifierApp\\monitor.ico",
        timeout = 10
    )
for i in range(4):
    time.sleep(21600)
    notificationn("Hey Vakit Geldi !!!",
                  "Dostum 6 saattir beni acik tutuyorsun, bellegim dolmaya basladi biraz uyuyup dinlenmeliyim.")


