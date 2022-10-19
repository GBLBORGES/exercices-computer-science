import random


def guess_name_game():
    list_names = ['rafaela', 'lia', 'belinda', 'diego', 'marcos']
    random_number = random.randrange(0, len(list_names))
    random_word = list_names[random_number]
    scrambled_word = "".join(random.sample(random_word, len(random_word)))
    print(scrambled_word)
    print('tente adivinhar qual é o nome')
    guesses = [input(), input(), input()]
    for guess in guesses:
        if guess == random_word:
            print("voce ganhou o jogo!! Parabens")
            return
    else:
        print('voce perdeu o jogo')


guess_name_game()



