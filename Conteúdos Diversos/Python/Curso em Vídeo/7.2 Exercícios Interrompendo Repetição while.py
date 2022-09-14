#Ex 66: Crie um programa que leia vários números. O programa só vai parar quando o usuário digitar o valor 999. No final mostre
#quantos números foram digitados e qual foi a soma entre eles.
s = 0
cont = 0
num = int(input('Digite um valor'))
while num != 999:
    s = s + num
    cont = cont + 1
    num = int(input('Digite um valor'))
print(f'Você digitou {cont} números e a soma foi {s}')

#Ex 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
#usuário. O programa será interrompido quando o número digitado for negativo.
num = int(input('Quer ver a tabuada de qual valor?'))
while num > 0:
    for c in range(1, 11):
        print(f'{num} * {c} = {num * c}')
    num = int(input('Quer ver a tabuada de qual valor?'))
print('Acabou')

#Ex 68: Faça um programa que jogue par ou ímpar. O jogo só será interrimpido se o jogador perder, mostrando o total
#de vitórias consecutivas que ele mostrou no final do jogo.
from random import randint
cont = 0
while True:
    jogador = int(input('Digite um número de 0 a 10.'))
    pc = randint(0, 10)
    jogada = input('Qual a sua jogada?[P/I]').upper()
    if jogada == 'I':
        jogadapc = 'P'
    else:
        jogadapc ='I'
    soma = jogador + pc
    if jogada == 'P' and soma % 2 == 0:
        print(f'Você colocou {jogador} e o computador colocou {pc}. Você venceu')
        cont = cont + 1
    elif jogada == 'I' and soma % 2 != 0:
        print(f'Você colocou {jogador} e o computador colocou {pc}. Você venceu')
        cont = cont + 1
    else:
        print(f'VocÊ colocou {jogador} e o computador colocou {pc}. O computador venceu')
        break
print(f'Acabou, você venceu {cont} vezes.')

#Ex 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá
#perguntar se o usuário quer ou não continuar. No final mostre quantos têm mais de 18 anos, quantos homens, e quantas
#mulheres com menos de 20 anos foram cadastradas.
cont = 0
homens = 0
mulheres = 0
total = 0
while True:
    idade = int(input('Idade:'))
    if idade > 18:
        cont = cont + 1
    sexo = input('Sexo: [M/F]').upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Qual o sexo').upper()
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1
    total = total + 1
    resp = input('Quer continuar?[S/N]').upper().strip()
    if resp == 'N':
        break
print(f'{total} pessoas foram cadastradas.\n{cont} pessoas tem mais de 18 anos.\n{homens} homens foram cadastrados.\n{mulheres} mulheres têm menos de 20 anos.')

#Ex 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar.
#No final mostre o total gasto na compra, quantos produtos custam mais de R$1000,00 e qual o nome do produto mais barato.
total = 0
cont = 0
totmil = 0
menor = 0
barato = ''
while True:
    produto = input('Produto:')
    preço = int(input('Preço:'))
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = input('Quer continuar?[S/N]').upper().strip()
    while resp != 'S' and resp != 'N':
        resp = input('Opção inválida. Quer continuar?[S/N]').strip().upper()
    if resp == 'N':
        break
print(f'O total gasto na compra foi {total:.2f}.\n{totmil} produtos custaram mais de R$1000,00\n{produto} foi o produto mais barato')

#Ex 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte qual o valor a ser sacado
#e o programa vai informar quantas cédulas de cada valor serão entregues. A caixa possui cédulas de 50,20,10 e 1.
valorSaque = int(input('Valor do saque: R$ '))
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')






