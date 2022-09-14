#Ex 28: Escreva um programa que pense em um número de 0 a 5 e peça ao jogador tentar acertar, o programa deverá
#escrever na tela se o jogador venceu ou perdeu.
from random import randint
print('Pensarei em um número entre 0 e 5')
num = randint(0,5)
chute = int(input('Tente adivinhar qual o número'))
if chute == num:
    print('Parabéns você acertou')
else:
    print(f'Hoje não Faro, o número era {num}')

#Ex 29: Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80 km/h ele será multado
#calcule a multa sendo que ela será R$7,00 para cada km acima do limite.
vel = float(input('Velocidade do carro'))
multa = (vel-80)*7
if vel<=80:
    print('Você está dentro do limite')
else:
    print('Você ultrapassou o limite de velocidade')
    print('A multá será de R$7,00 para cada km acima do limite')
    print(f'O valor da multa será {multa}')

#Ex 30: Crie um programa que leia um número e diga se ele é par ou ímpar.
from time import sleep
num = int(input('Digite um número'))
print('_'*20)
print('PROCESSANDO')
print('-'*20)
sleep(2)
if num % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

#Ex 31: Crie um programa que calcule a distância de uma viagem em km e calcule o preço da passagem cobrando
#R$0,50 por km para até 200 km ou R$0,45 por km para viagens mais longas.
dist = float(input('Qual a distância em km?'))
if dist<=200:
    valorf = dist*0.5
    print(f'O valor a se pagar será R$ {valorf}')
else:
    valorf = dist*0.45
    print(f'O valor a se pagar será R${valorf}')

#Ex 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o último número: '))
if num1 == num2 and num1 == num3 and num2 == num3:
    print('Todos os valores são iguais')
else:
    if num1 >= num2 and num1 >= num3:
        maior = num1
    if num2 >= num1 and num2 >= num3:
        maior = num2
    if num3 >= num1 and num3 >= num2:
        maior = num3
    print('O número {} é o maior...'.format(maior))
    if num1 <= num2 and num1 <= num3:
        menor = num1
    if num2 <= num1 and num2 <= num3:
        menor = num2
    if num3 <= num1 and num3 <= num2:
        menor = num3
    print('E o número {} é o menor'.format(menor))

#Ex 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para
#salários superiores a R$1.250,00 calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
sal = float(input('Qual o seu salário?'))
if sal > 1250:
    salf = sal + (sal*0.10)
    print(f'Seu novo salário será R${salf}')
elif sal <= 1250:
    salf = sal + (sal*0.15)
    print(f'Seu novo salário será R${salf}')










