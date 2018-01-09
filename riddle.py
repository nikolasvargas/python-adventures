""" jogo simplório """
import random as _random
import playground

def run():
    """ game start """

    playground.welcome()

    random_number = _random.randrange(1, 101)
    game_round = 1
    find = False
    easy = 1
    intermediary = 2
    hard = 3
    attempts = 0

    game_level = int(input("em qual nível quer jogar? facil(1) intermediário(2) difícil(3): "))

    if game_level == easy:
        attempts = 20
    elif game_level == intermediary:
        attempts = 10
    elif game_level == hard:
        attempts = 5

    points = 1000

    for game_round in range(1, attempts + 1):
        print("rodada {} de {} :".format(game_round, attempts))

        game_round = game_round + 1

        customer_number = int(input("digite um numero entre 0 e 100: "))

        if (customer_number < 1 or  customer_number > 100):
            print('... {}'.format(customer_number), end='\n')
            continue

        find = random_number == customer_number
        maior = customer_number > random_number
        menor = customer_number < random_number

        if find:
            print("bingo! você acertou!! o número é {}".format(random_number), end='\n')
            print("sua pontuação final é: {}".format(points), end='\n')
            restart(int(input("jogar novamente?: sim(1) nao(0): ")))
            break
        else:
            if maior:
                print("maior do que o numero random", end='\n')
                points = points - abs(customer_number - random_number)

            elif menor:
                print("menor que o numero random", end='\n')
                points = points - abs(random_number - customer_number)

    if not find:
        print('você perdeu e suas tentativas acabaram', end='\n')
        restart(int(input("jogar novamente?: sim(1) nao(0): ")))

print("fim de jogo", end='\n')

def restart(decision):
    """ reinicar o jogo """
    if decision == 1:
        run()
    else:
        print("fim da execução")

if __name__ == '__main__':
    run()
