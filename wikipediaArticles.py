import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    html = BeautifulSoup(response.content, "html.parser")
    title = html.find(class_="firstHeading").text

    print(title)
    cevap = input("Siteyi acmami istermisin (E/H, cikmak icin q'ya basin)? ").lower()

    if cevap == "e":
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/title")
        continue
    elif cevap == "q":
        print("Uygulamadan cikiliyor.")
        break
    elif cevap == "h":
        continue
    else:
        print("Yanlis karakter girisi")
        break