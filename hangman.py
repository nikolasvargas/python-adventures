""" another game """
import random as _random
def run():
    """ run the game """

    print("*****************************************")
    print("*********** Bem vindo ao jogo! **********")
    print("*****************************************")

    external_word_list = []

    with open("./array_words.txt") as data:
        for word_list in data:
            external_word_list.append(word_list.strip())

    secret_word = external_word_list[_random.randrange(0, len(external_word_list))].upper()
    letter_spacing = ["_" for l in secret_word] #list comprehension

    # while len(letter_spacing) < len(secret_word):
    #     letter_spacing.append("_")

    die = False
    win = False
    attemps = 6
    wrongs = 0

    while(not win and not die):

        letter = input("Digite uma letra: ").upper().strip()
        index = 0

        if letter in secret_word:

            for word in secret_word:
                if letter == word:
                    letter_spacing[index] = letter

                index += 1

        else:
            wrongs += 1
            print("{} erros de {}".format(wrongs, attemps), end='\n')

        if wrongs == attemps:
            print("você atingiu o número máximo de erros permitidos", end='\n')
            print("fim de jogo", end='\n')
            break
        else:
            print("você ainda tem {} tentativas".format(attemps - wrongs), end='\n')

        if "".join(tuple(letter_spacing)) == secret_word.upper():
            print("you win!!", end='\n')
            print("quantidade de erros: {}".format(wrongs), end='\n')
            break
        else:
            print(" ".join(tuple(letter_spacing)), end='\n')


if __name__ == '__main__':
    run()
