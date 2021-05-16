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
        
        linha_aleatoria = random.randrange(1,sum(1 for _ in arquivo)) # Seleciona uma linha aleartória do arquivo

        #Busca palavra específica
        arquivo = open('palavras', 'r')
        palavra = (arquivo.readlines()[linha_aleatoria])
        arquivo.close
        return palavra

def esconde_palavra():
    palavra = escolhe_palavra()
    tracos = []
    for _ in palavra: #Não salvando a variavel na memória 
        tracos.append('_')
    return palavra, tracos


def verifica_jogo(acertos, erros, palavra):
    if acertos >= len(palavra)-1:
        print('Parabens! Você ganhou o jogo')

    elif erros == len(HANGMANPICS)-1:
        print('Game Over!')
        print('A palavra era: %s ' %(palavra))


def inicia_jogo():
    palavra, tracos = esconde_palavra()
    acertos, erros = 0, 0

    while (erros != len(HANGMANPICS)):
        print(HANGMANPICS[erros]) 
        print(''.join(tracos[:-1]))
        i = 0
        escolha = input('Digite uma letra: ').upper()

        if escolha in palavra:
            for _ in palavra: #Para não guardar a variável na memória
                if escolha in palavra[i]:
                    tracos[i] = _
                    acertos += 1
                i+=1

        else:
            erros +=1
    verifica_jogo(acertos, erros, palavra)

def main():
    inicia_jogo()

if __name__ == '__main__':
    inicia_jogo()

#Coisas que faltam segundo @Cussa me indicou na mentoria
# 1 - Verificar se o usário não digitou a letra e esta digitando novamente a mesma letra
# 2 - Verificar se o usuário digitou um caracter inválido ou algo desse tipo.
