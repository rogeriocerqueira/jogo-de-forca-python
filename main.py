import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def escolhe_palavra():
    with open('palavras.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    return random.choice(linhas).strip().upper()

def esconde_palavra():
    palavra = escolhe_palavra()
    tracos = ['_' for _ in palavra]
    return palavra, tracos

def verifica_jogo(acertos, erros, palavra):
    if acertos >= len(palavra):
        print('Parabéns! Você ganhou o jogo')
    else:
        print('Game Over!')
        print(f'A palavra era: {palavra}')

def inicia_jogo():
    palavra, tracos = esconde_palavra()
    acertos, erros = 0, 0
    letras_escolhidas = []
    print(HANGMANPICS[0])
    print(' '.join(tracos))

    while erros < len(HANGMANPICS) - 1 and acertos < len(palavra):
        while True:
            escolha = input('Digite uma letra: ').upper()
            if len(escolha) == 1 and escolha.isalpha():
                break
            print("Entrada inválida. Digite apenas uma letra.")

        if escolha in letras_escolhidas:
            print("Você já escolheu essa letra. Tente outra.")
            continue

        letras_escolhidas.append(escolha)

        if escolha in palavra:
            for i, letra in enumerate(palavra):
                if escolha == letra:
                    tracos[i] = letra
                    acertos += 1
        else:
            erros += 1

        print(HANGMANPICS[erros])
        print(' '.join(tracos))

    verifica_jogo(acertos, erros, palavra)

if __name__ == '__main__':
    while input('Deseja jogar? (S/N): ').upper() == 'S':
        inicia_jogo()
