""" another game """
import random as _random
import playground

def run():
    """ run the game """

    playground.welcome()

    external_word_list = []

    try:
        with open("./array_words.txt") as data:
            for word_list in data:
                external_word_list.append(word_list.strip())

    except (IOError) as identifier:
        print('Read error: {}'.format(identifier))

    finally:
        print('done')

    secret_word = external_word_list[_random.randrange(0, len(external_word_list))].upper()
    letter_spacing = ["_" for l in secret_word] #list comprehension

    # while len(letter_spacing) < len(secret_word):
    #     letter_spacing.append("_")

    die = False
    win = False
    attemps = 7
    wrongs = 0
    letters_typed = []

    while(not win and not die):

        letter = input("Digite uma letra: ").upper().strip()
        letters_typed.append(letter)

        index = 0

        if letter in secret_word:

            for word in secret_word:
                if letter == word:
                    letter_spacing[index] = letter

                index += 1

        else:
            wrongs += 1
            print("{} jogada de {}".format(wrongs, attemps), end='\n')

        if wrongs == attemps:
            die = True
        else:
            handman_die(wrongs)
            print("você ainda tem {} tentativas".format(attemps - wrongs), end='\n')
            print("letras já inseridas:")
            print(" ".join(tuple(letters_typed)), end='\n')

        if "".join(tuple(letter_spacing)) == secret_word.upper():
            win = True
        else:
            print(" ".join(tuple(letter_spacing)), end='\n')

        if win:
            playground.win_print()
            print("quantidade de erros: {}".format(wrongs), end='\n')
        elif die:
            lose_print()

def lose_print():
    print("você atingiu o número máximo de erros permitidos", end='\n')
    print("fim de jogo", end='\n')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def handman_die(wrongs):
    print("  _______     ")
    print(" |/      |    ")

    if(wrongs == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(wrongs == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(wrongs == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (wrongs == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    run()
