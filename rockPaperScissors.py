import random

def play(user, computer):
    dictionary = {
        3: "paper",
        2: "rock",
        1: "scissors"
    }
    if user == computer:
        print("User: {}\tComputer: {}\nBerabere".format(dictionary[user],dictionary[computer]))
    elif (user == 3 and computer == 1) or (user == 1 and computer == 3):
        if user == 1:
            print("User: {}\tComputer: {}\nTebrikler kazandin.".format(dictionary[user],dictionary[computer]))
        else:
            print("User: {}\tComputer: {}\nMaalesef kaybettin.".format(dictionary[user],dictionary[computer]))
    elif (user > computer):
        print("User: {}\tComputer: {}\nTebrikler kazandin.".format(dictionary[user],dictionary[computer]))
    elif (computer > user):
        print("User: {}\tComputer: {}\nMaalesef kaybettin.".format(dictionary[user],dictionary[computer]))

while True:
    user = input("Paper = 3, Rock = 2, Scissors = 1\nEnter number (Cikmak icin 0 gir): ")
    computer = random.randint(1,3)
    if user.isdigit():
        user = int(user)
        if user <= 3 and user >= 0:
            if user == 0:
                print("Tekrar gorusmek uzere.")
                break
        else:
            print("Lutfen 0,1,2 ve 3 sayilarindan birini girmeyi dene")
            continue
    else:
        print("Bir daha ki sefere belirtilen sayilardan birini girmeyi dene.")
        break
    play(user,computer)

