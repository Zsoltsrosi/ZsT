import random, os, sys

List = ["Tirana", "Yerevan", "Vienna", "Baku", "Wakanda",
        "Minsk", "Brussels", "Sarajevo", "Sofia", "Zagreb", "Nicosia", "Prague",
        "Copenhagen", "Tallinn", "Helsinki", "Paris", "Tbilisi", "Berlin", "Athens",
        "Budapest", "Reykjavik", "Dublin", "Rome", "Pristina", "Riga",
        "Vaduz", "Vilnius", "Luxembourg", "Valletta", "Monaco",
        "Podgorica", "Amsterdam", "Skopje", "Oslo", "Warsaw", "Lisbon", "Bucharest", "Moscow",
        "Belgrade", "Bratislava", "Ljubljana", "Madrid", "Stockholm", "Bern",
        "Ankara", "Kyiv", "London", ]
city = (random.choice(List))
word = city.upper()
word_list = list(word)
i = len(word)
displayed = ["_ "] * i
tippelt_betu = []


def uncover(hashed_password, password, letter):
    for i in range(len(word)):
        if word[i] == letter:
            displayed[i] = word[i]


def is_win():
    print("""\

     ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
     ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
      ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
       ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
        ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
        ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                               """)
    print("You were correct!\nThe answer was: ", word)


def is_loose():
    print("""\

      ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███   ▐██▌
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒ ▐██▌
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒ ▐██▌
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄   ▓██▒
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒ ▒▄▄
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▀▀▒
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░ ░  ░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░     ░
          ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░      ░
                                                         ░   
    """)
    print("Correct answer was: ", word)


def start_manu():
    life_points = 10
    # Import Life to manu, send it to input, change pass to get_input(Life_points), add difficulty choose screen and,
    # get get_input() off of main.
    print("""\

           ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄
          ███    ███     ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄
          ███    ███     ███    ███ ███   ███   ███    █▀  ███   ███   ███   ███    ███ ███   ███
         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███        ███   ███   ███   ███    ███ ███   ███
        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ███   ███   ███ ▀███████████ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    █▀      ███    █▀   ▀█   █▀    ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀

        """)

    start_choice = input("Do you want to play a gem? (Y/N) :  ")
    if start_choice == "Y":
        os.system("clear")
        print("""\

           ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄
          ███    ███     ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄
          ███    ███     ███    ███ ███   ███   ███    █▀  ███   ███   ███   ███    ███ ███   ███
         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███        ███   ███   ███   ███    ███ ███   ███
        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ███   ███   ███ ▀███████████ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    █▀      ███    █▀   ▀█   █▀    ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀

        """)

        get_input(life_points)
    elif start_choice == "N":
        no_choice = input("Are you sure about that?? (Y/N) :  ")
        if no_choice == "Y":
            sys.exit()
        elif no_choice == "N":
            os.system("clear")
            print("""\

           ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄
          ███    ███     ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄
          ███    ███     ███    ███ ███   ███   ███    █▀  ███   ███   ███   ███    ███ ███   ███
         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███        ███   ███   ███   ███    ███ ███   ███
        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ███   ███   ███ ▀███████████ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    █▀      ███    █▀   ▀█   █▀    ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀

        """)

        get_input(life_points)
    else:
        sys.exit()


def get_input(life_points):
    cheat = "CHEAT"
    print("\n")
    while life_points > 0:
        print("".join(displayed))
        print("Life Points: ", life_points)
        guess1 = input("Guess a letter: ")
        os.system("clear")
        print("""\

           ▄█    █▄       ▄████████ ███▄▄▄▄      ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄
          ███    ███     ███    ███ ███▀▀▀██▄   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄
          ███    ███     ███    ███ ███   ███   ███    █▀  ███   ███   ███   ███    ███ ███   ███
         ▄███▄▄▄▄███▄▄   ███    ███ ███   ███  ▄███        ███   ███   ███   ███    ███ ███   ███
        ▀▀███▀▀▀▀███▀  ▀███████████ ███   ███ ▀▀███ ████▄  ███   ███   ███ ▀███████████ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    ███     ███    ███ ███   ███   ███    ███ ███   ███   ███   ███    ███ ███   ███
          ███    █▀      ███    █▀   ▀█   █▀    ████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀

        """)
        guess2 = guess1.upper()
        if guess2 in tippelt_betu:
            print(tippelt_betu)
            print("You already guessed this letter! Try another one!")
        else:
            tippelt_betu.append(guess2)
            uncover(None, None, guess2)
            if guess2 == word:
                os.system("clear")
                is_win()
                break
            elif word_list == displayed:
                os.system("clear")
                is_win()
                break
            elif guess2 == cheat:
                del tippelt_betu[-1]
                print(tippelt_betu)
                print(word)
            elif len(guess2) == 1:
                if guess2.isalpha():
                    print(tippelt_betu, "\n")
                    if guess2 not in word:
                        life_points -= 1
                else:
                    del tippelt_betu[-1]
                    print(tippelt_betu)
                    print("Please guess a letter from the alphabet!!")
            elif len(guess2) != 1:
                del tippelt_betu[-1]
                print(tippelt_betu)
                print("Only guess 1 letter!")
            else:
                pass
    if life_points == 0:
        os.system("clear")
        is_loose()


os.system("clear")


def main():
    start_manu()


if __name__ == '__main__':
    main()
