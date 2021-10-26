email = input("Email adresini gir: ")
index = email.find("@")

if index == -1:
    print("Bir daha ki sefere '@' sembolu iceren email adresini girmeyi dene.")
    quit()

username = email[:index]
domainName = email[index:]

print("Kullanici adi: {}\nDomain: {}".format(username, domainName))
    

