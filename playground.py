""" main of main """
import riddle
import hangman

def main():
    """ start select """

    print("***************************************************", end="\n")
    print("*********** Bem vindo ao salão de jogos! **********", end="\n")
    print("***************************************************", end="\n")

    print("***** (1) hangman game <---> (2) riddle game *****")
    game_choise = int(input("escolha o game: "))

    if game_choise == 1:
        hangman.run()
    elif game_choise == 2:
        riddle.run()

def play_again():
    """play again"""
    main()

def welcome():
    """ zzZZZzzzzZZZzzzzzz """
    print("*****************************************")
    print("*********** Bem vindo ao jogo! **********")
    print("*****************************************")

def win_print():
    print("Winner!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if __name__ == '__main__':
    main()
