import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]
while True:
    liste = ['javascript', 'node.js', 'kalilinux', 'sql', 'lite', 'jquery']
    kelime = random.choice(liste)
    tahmin = []
    adim = 0
    while True:
        print(resim[adim])
        for i, char in enumerate(kelime, start=1):
            print(char if i in tahmin else "_")
        
        if adim >= (len(resim)-1):
            print('Maalesef butun parcalar birlesti ve hakkin bitti')
            break
        elif len(kelime) <= adim:
            print('Kelime ortaya cikti ve katbettin')
            break
        
        cevap = input("Aklindaki kelimeyi gir: ")
        
        if cevap == kelime:
            print(cevap)
            print('Kelimeyi dogru bilgin dostum tebrik ederim')
            break
        else:
            while True:
                rastgele = random.randint(1,len(kelime))
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break
            adim += 1
    soru = input('Oyuna devam etmek istiyormusun (devam etmek icin y tusuna basman yeterli): ')
    if "y" == soru:
        print("Devam etmene sevindim, senin icin baska bir kelime sectim hadi tahmin et;")
    else:
        print("Ayrilmana uzuldum umarim tekrar gorusuruz dostum kendine iyi bak.")
        break
            

        
        


