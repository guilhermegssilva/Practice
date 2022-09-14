#Ex 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura, comprimento)
#e mostre a área do terreno.
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a} metros quadrados.')

l = int(input('Largura:'))
c = int(input('Comprimento'))
área(l, c)

#Ex 97: Faça um programa que tenha uma função escreva(), que receba um texto como parámetro e mostre uma mensagem com tamanho
#adaptável.
def escreva(mensagem):
    tamanho = len(mensagem)
    print('-' * tamanho)
    print(mensagem)
    print('-' * tamanho)
escreva('Olá mundo')

#Ex 98: Faça um programa que tenha uma função chamada contador(), e recebe três parâmetros, início, fim e passo e realize a
#contagem. Seu programa tem que realizar três contagens: De 1 até 10 de 1 em 1, de 10 até 0 de 2 em 2, e uma contagem personalizada.
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{c} ', end='')
            cont = cont + p
    else:
        cont = i
        while cont >=f:
            print(f'{cont} ',end=True)
            cont = cont - p

contador(1, 2, 3)
contador(10, 0, 2)
contador(0)
ini = int(input('Início:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)

#Ex 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com números inteiros. Seu programa
#deve analisar todos eles e dizer qual deles é o maior.
def maior(*num):
    Maior = 0
    cont = 0
    for c in num:
        if c > Maior:
            Maior = c
        cont = cont + 1
    print(f'Foram informados {cont} valores e o mais alto é {c}.')
maior(2)
maior(1, 7, 9)
maior(1, 2, 3)
maior(0, 0)

#Ex 100: Faça um programa que tenha uma lista chamada números e duas funções, chamadas sorteia() e somapar(). A primeira função
#vair sortear 5 números e colocá-los dentro de uma lista e a segunda vai mostrar a soma de todos os valores pares dela.
from random import randint
números = []
def sorteia(num):
    for c in range(0, 5):
        números.append(randint(0, 10))
    print(f'Os números sorteados foram {números}.')
sorteia(números)

def soma(num):
    s = 0
    for c in números:
        if c % 2 == 0:
            s = s + c
    print(f'A soma dos números pares foi {s}.')
soma(números)
