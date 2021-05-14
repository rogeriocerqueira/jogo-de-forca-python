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
            sorteia = random.randrange(1, len(linhas))
            linhas = linhas[sorteia]
            return linhas[:-1]

def esconde_palavra():
    palavra = escolhe_palavra()
    tracos = []
    for _ in palavra:
        tracos.append('_')
    return palavra, tracos

def verifica_jogo(acertos, erros, palavra):
    if acertos >= len(palavra) and erros != len(HANGMANPICS)-1:
        print('Parabens! Você ganhou o jogo')

    else:
        print('Game Over!')
        print('A palavra era: %s ' %(palavra))


def analisa_letra(escolha, lista): # Guarda as letras escolhidas pelo usuario em uma lista de valores

    for caracter in lista:
        if escolha == caracter:
            return True, lista

    lista.append(escolha)
    return False, lista


def inicia_jogo():
    print(HANGMANPICS[0]) #Mostra a forca logo de inicio
    palavra, tracos = esconde_palavra()
    print(''.join(tracos))
    acertos, erros = 0, 0
    lista = ['*']  # Aqui eu inicializei a lista com um valor qualquer só pra não ocorrer erro

    while (erros != len(HANGMANPICS)-1) and acertos < len(palavra):
        i = 0
        escolha = input('Digite uma letra: ').upper()

        if escolha in palavra:
            for _ in palavra:
                if escolha in palavra[i]:
                    tracos[i] = _
                    acertos += 1
                i+=1

        else:
            print(HANGMANPICS[erros+1]) #Proximo elemento da lista
            erros +=1

        print(''.join(tracos))
        print(acertos, (len(palavra)))

    verifica_jogo(acertos, erros, palavra)

if __name__ == '__main__':
    inicia_jogo()
    # escolhe_palavra()
