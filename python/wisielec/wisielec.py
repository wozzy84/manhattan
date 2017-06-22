import sys
import random

def main_menu():
    print("Witaj w programie wisielec")
    print("Co chcesz zrobić?")
    print("1. Nowa gra")
    print("2. Zakończ")

def read_user_input():
    user_input = input()
    print("Wybrałeś:", user_input)
    return user_input

def play(user_input):
    if user_input == "1":
        run()
    elif user_input == "2":
        print("Miło Cię było widzieć")
        sys.exit()

def run():
    print("Gramy")
    word = pick_word()
    already_guessed = []
    while liczba_prob > 0 and still_not_guessed(word, already_guessed):
        print("Odgadnięte:")
        print_word(word, already_guessed)
        print("Podaj wyraz:")
        char = input()
        already_guessed.append(char)

    print("Wyraz: ")
    print_word(word, already_guessed)
    print("Gratulacje! Wygrana")

def pick_word():
    return random.choice([
        "sok",
        "tłok",
        "bok"
    ])

def print_word(word, already_guessed):
    for c in word:
        if c in already_guessed:
            print(c, " ", end="")
        else:
            print("_", " ", end="")
    print()

def still_not_guessed(word, already_guessed):
    for letter in word:
        if letter not in already_guessed:
            return True

    return False

if __name__ == "__main__":
    while True:
        main_menu()
        user_input = read_user_input()
        play(user_input)
