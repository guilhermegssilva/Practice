#Ex 57: Faça um programa que leia o sexo de uma pessoa mais só aceite os valores
#'M' ou 'F', caso esteja errado diga que a opção foi inválida.
r = input('Qual o seu sexo').upper()
while r != 'M' and r != 'F':
    r = input('Opção inválida, digite seu sexo.').upper()
print(f'Seu sexo {r} foi registrado com sucesso')
print('Fim')

#Ex 58: Melhore o jogo da adivinhação onde o computador vai pensar em um número entre 0 e 10 e o
# jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer.
from random import randint
cont = 1
r = randint(0,2)
num = int(input('Digite um número'))
while num != r:
    if num > r:
        num = int(input('Resposta errada, é menor'))
        cont = cont + 1
    elif num < r:
        num = int(input('Resposta errada, é maior'))
        cont = cont + 1
    elif num == r:
        cont = cont + 1
print(f'Certa resposta, você precisou de {cont} tentativas')

# Ex 59: Crie um programa que leia dois valores e mostre na tela um menu de opções (multiplicar, somar, maior,
# novos números, sair do programa). Seu programa deverá realizar a opção solicitada em cada caso.

num1 = int(input('Digite um valor'))
num2 = int(input('Digite outro valor'))
opçao = 0
while opçao !=5:
    opçao = int(input('Oque deseja fazer?\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa'))
    if opçao == 1:
        print(num1 + num2)
    elif opçao == 2:
        print(num1 * num2)
    elif opçao == 3:
        print(max(num1,num2))
    elif opçao == 4:
        num1 = int(input('Digite um valor'))
        num2 = int(input('Digite outro valor'))
    elif opçao == 5:
        print('Obrigado')
    elif opçao > 5:
        print('Opção inválida')

#Ex 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input('Qual o número?'))
cont = 0
fat = 1
while cont < num:
    if num < 0:
        print('Deve ser um número positivo')
    else:
        cont = cont + 1
        fat = fat * cont
print(f'O fatorial de {num} é {fat}.')

#Ex 61: Faça um gerador de PA que leio o primeiro termo e a razão e mostre os 10 primeiros termos da progressão.
primeiro = int(input('Qual o primeiro termo?'))
razão = int(input('Qual a razão?'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    cont = cont + 1
    termo = termo + razão

#Ex 62: Faça um gerador de PA que pergunte se o usuário quer mostrar mais algum termo, o programa para se ele digitar
#que quer ver mais 0 termos.
primeiro = int(input('Qual o primeiro termo?'))
razão = int(input('Qual a razão?'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}')
    cont = cont + 1
    termo = termo + razão
num = int(input('Quer ver mais quantos termos?'))
if num == 0:
    print('Até mais!')
else:
    cont1 = 1
    while cont1 <= num:
        print(f'{termo}')
        cont1 = cont1 + 1
        termo = termo + razão

#Ex 63: Escreva um programa que mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
elementos = int(input('Quantos elementos na sequência?'))
cont = 3
t1 = 0
t2 = 1
print(t1,t2, end=' ')
while cont <= elementos:
    t3 = t1 + t2
    print(t3, end=' ')
    cont = cont + 1
    t1 = t2
    t2 = t3

#Ex 64: Crie um programa que leia vários números inteiros pelo teclado, o programa só vai parar quando o usuário
#digitar o valor de 999. No final diga quantos números foram digitados e qual foi a soma entre eles.
num = 0
soma = 0
cont = 0
num = int(input('Digite um número'))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input('Digite um número'))
print(f'Você digitou {cont} números e a soma deles é {soma}')

#Ex 65: Crie um programa que leia vários números inteiros. No final mostre a média entre eles e o maior e menor valor.
#O programa deve perguntar se o usuário quer ou não continuar a digitar valores.
lista = []
resposta = 'S'
soma = 0
cont = 0
while resposta == 'S':
    num = int(input('Digite um número'))
    resposta = input('Quer continuar?[S/N]').upper()
    lista.append(num)
    soma = soma + num
    cont = cont + 1
print(f'A média dos números será {soma/cont}, o maior número foi {max(lista)} e o menor foi {min(lista)}')


















