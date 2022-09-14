#Ex 72: Crie uma tupla com os números de 0 a 20 por extenso. Seu programa deverá ler um número pelo teclado e
#mostrá-lo por extenso.
números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20:'))
while num > 20 or num < 0:
    num = int(input('Resposta inválida.Tente de novo.'))
else:
    print(f'Você digitou o número {números[num]}')

#Ex 74: Crie um programa que gere 5 números aleatórios e os coloque numa tupla. Depois disso mostre a listagem dos
#números gerados e também indique qual é o de maior e menor valor.
from random import randint
lista_números = []
for c in range(0,5):
    num = randint(0, 10)
    lista_números.append(num)
print(f'Os valores sorteados são {lista_números}.')
print(f'O valor mais alto é {max(lista_números)}')
print(f'O valor mais baixo é {min(lista_números)}')

#Ex 75: Desenvolva um programa que leia quatro valores pelo teclado e no mostre: Quantas vezes apareceu o número 4
#em que posição foi digitado o valor 3 e quais foram os números pares.
números = []
cont = 0
for c in range(0,4):
    num = int(input('Digite um número:'))
    números.append(num)
    if num % 2 == 0:
        cont = cont + 1
print(f'O número 9 apareceu {números.count(9)} vezes.')
if números.count(3) == 0:
    print('O número 3 não apareceu nenhuma vez')
else:
    print(f'O número 3 foi digitado primeiro na {(números.index(3))+1}ª posição.')
print(f'No total foram {cont} números pares.')

#Ex 77: Crie um programa que tenha uma tupla com várias palavras, depois disso você deve mostrar para cada palavra quais
#são as suas vogais.
lista = ['aprender', 'estudar', 'linguagem', 'python', 'futuro', 'mercado', 'praticar']
for c in lista:
    print(f'\nNa palavra {c} temos as vogais', end=' ')
    for vogais in c:
        if vogais in 'aeiou':
            print(f'{vogais}', end=' ')








