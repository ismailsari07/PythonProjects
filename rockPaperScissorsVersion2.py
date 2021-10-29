import random
import math

def play():
    user = input("Senin secimin hangisi? tas icin 't', kagit icin 'k', makas icin 'm': \n")
    computer = random.choice(['t','k','m'])

    if user == computer:
        return(0, user, computer)
    if is_win(user,computer):
        return(1, user, computer)
    return(-1, user, computer)

def is_win(player,opponent):
    if (player == "t" and opponent == "m") or (player == "k" and opponent == "t") or (player == "m" and opponent == "k"):
        return True
    return False

def play_best_of(n):
    user_wins = 0
    computer_wins = 0
    wins_necesarry = math.ceil(n/2)
    while user_wins < wins_necesarry and computer_wins < wins_necesarry:
        result, user, computer = play()
        #berabere
        if result == 0:
            print("User: {}\tComputer: {}\nBerabere".format(user, computer))
        elif result == 1:
            user_wins += 1
            print("User: {}\tComputer: {}\nKazandin!".format(user, computer))
        else:
            computer_wins += 1
            print("User: {}\tComputer: {}\nKaybettin :(".format(user, computer))
        print("\n")
    if user_wins > computer_wins:
        print(f"Gayet iyi bir oyun cikardin, {wins_necesarry} kere galip gelerek kazandin.")
    else:
        print(f"Bilgisayar {wins_necesarry} kere yenerek galip geldi\nKafana takma bir daha ki sefere kazanabilirsin.")

if __name__ == '__main__':
    print(play_best_of(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
