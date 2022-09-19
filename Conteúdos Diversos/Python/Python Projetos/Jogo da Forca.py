from random import choice
imagem = [r"""
                   ________
                   |      |
                   |     ( )
                   |     /|\
                   |      |
                   |     / \
                   |
                """,
                r"""
                   ________
                   |      |
                   |     ( )
                   |     /|\
                   |      |
                   |     / 
                   -
                """,
                r"""
                   ________
                   |      |
                   |     ( )
                   |     /|\
                   |      |
                   |      
                   -
                """,
                r"""
                   ________
                   |      |
                   |     ( )
                   |     /|
                   |      |
                   |     
                   -
                """,
                """
                   ________
                   |      |
                   |     ( )
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   ________
                   |      |
                   |     ( )
                   |    
                   |      
                   |     
                   -
                """]
palavras = ['cavalo', 'baleia', 'rinoceronte', 'borboleta', 'elefante', 'alce', 'tamandua', 'canguru', 'joaninha']

palavras_apoio = ['Muito bem', 'Isso aí', 'Continue assim', 'Correto', 'Parabéns', 'Muito bom']
print('BEM VINDO AO JOGO DA FORCA.\nSEU OBJETIVO É TENTAR ADIVINHAR A PALAVRA ANTES DE FICAR SEM TENTATIVAS')
print('VAMOS COMEÇAR!!!')
print()
palavra = list(choice(palavras))
oculto = list('_' * len(palavra))
print(' '.join(oculto))
print()
chances = 6
cont = 0
usadas = []
print(f'Você tem {chances} chances restantes')
palpite = input('Digite uma letra: ').lower()
while True:
    while palpite in usadas:
        palpite = input('Essa letra já foi\nEscolha outra letra: ').lower()
    if palpite.isalpha() and len(palpite) == 1:
        usadas.append(palpite)
        if palpite not in palavra:
            print(imagem[chances - 1])
            chances = chances - 1
            cont = cont + 1
            if chances == 0:
                break
            print(f'Não existe a letra {palpite} nesta palavra.\nVocê tem {chances} chances restantes.')
            print(f'Letras usadas: {",".join(usadas)}')
            palpite = input('Escolha uma letra:').lower()
        else:
            for c, l in enumerate(palavra):
                if palavra[c] == palpite:
                    oculto[c] = palpite
            print()
            print(' '.join(oculto))
            print()
            cont = cont + 1
            if oculto == palavra:
                break
            palpite = input(f'{choice(palavras_apoio)}\nDigite outra letra: ').lower()
    else:
        palpite = input('São aceitas apenas letras únicas. Por favor digite uma letra: ').lower()

print(f'A palavra era {"".join(palavra)}')
if chances == 0:
    print('Que pena, você perdeu! :(')
else:
    print(f'PARABÉNS, VOCÊ VENCEU!!!\nVocê precisou de {cont} tentativas para descobrir a palavra')