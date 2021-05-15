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
    with open('palavras') as arquivo:
            linhas = arquivo.readlines()
            linhas = linhas[random.randrange(1, len(linhas))]
            return linhas[:-1]

def esconde_palavra():
    palavra = escolhe_palavra()
    tracos = []
    for caracter in palavra:
        tracos.append('_')
    return palavra, tracos


def verifica_jogo(acertos, erros, palavra):
    if acertos >= len(palavra):
        print('Parabens! Você ganhou o jogo')

    elif erros == len(HANGMANPICS)-1:
        print('Game Over!')
        print('A palavra era: %s ' %(palavra))


def inicia_jogo():
    palavra, tracos = esconde_palavra()
    acertos, erros = 0, 0

    while (erros != len(HANGMANPICS)):
        i = 0
        escolha = input('Digite uma letra: ').upper()

        if escolha in palavra:
            for caracter in palavra:
                if escolha in palavra[i]:
                    tracos[i] = caracter
                    acertos += 1
                i+=1

        else:
            print(HANGMANPICS[erros+1]) #Imprime a posição seguinte da lista e não a primeira
            erros +=1

        if acertos >= len(palavra):
            break

        print(''.join(tracos))
    verifica_jogo(acertos, erros, palavra)

def main():
    inicia_jogo()

if __name__ == '__main__':
    inicia_jogo()
