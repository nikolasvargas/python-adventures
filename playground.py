""" main of main """
from __future__ import print_function
import riddle
import hangman

def main():
    """ start select """

    print("***************************************************", end="\n")
    print("*********** Bem vindo ao salão de jogos! **********", end="\n")
    print("***************************************************", end="\n")

    game_choise = int(input("hangman game(1) riddle game(2): "))

    if game_choise == 1:
        hangman.run()
    elif game_choise == 2:
        riddle.run()

if __name__ == '__main__':
    main()
