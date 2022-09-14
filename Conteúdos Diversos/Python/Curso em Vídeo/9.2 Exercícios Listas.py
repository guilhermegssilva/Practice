#Ex 84: Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final mostre: Quantas pessoas
#foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves.
lista = []
pessoas = []
maior = 0
menor = 999
while True:
    pessoas.append(input('Qual o seu nome?'))
    pessoas.append(int(input('Qual seu peso?')))
    lista.append(pessoas[:])
    pessoas.clear()
    resposta = input('Quer continuar?[S/N]').upper()
    if resposta == 'N':
        break
for c in lista:
    if c[1] > maior:
        maior = c[1]
    if c[1] < menor:
        menor = c[1]
print(f'Foram cadastradas {len(lista)} pessoas.')
for c in lista:
    if c[1] == maior:
        print(f'O maior peso foi de {c[0]} com {maior}Kg.')
for c in lista:
    if c[1] == menor:
        print(f'O menor peso foi de {c[0]} com {menor}Kg.')

#Ex 85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separado os valores páres do valores ímpares. Ao final, mostre os valores em ordem crescente.
lista = []
pares = []
ímpares = []
for c in range(1,8):
    num = int(input(f'Digite o {c}° número:'))
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
pares.sort()
ímpares.sort()
lista.append(pares)
lista.append(ímpares)
print(f'Os números pares digitados foram {lista[0]}')
print(f'Os números ímpares digitados foram {lista[1]}')

#Ex 86: Crie uma matriz de dimensão 3X3 e a preencha com valores lidos pelo teclado, no final mostre a matriz na tela.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input('Digite um número:'))
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]}]',end=' ')
    print()

#Ex 87: Aprimore o desafio anterior mostrando no final: A soma de todos os valores pares digitados, a soma dos valores da
#terceira coluna, e o maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input('Digite um número'))
        if matriz[c][l] % 2 == 0:
            somapar = somapar + matriz[c][l]
somacol = 0
for c in range(0, 3):
    somacol = somacol + matriz[c][2]

print(f'A soma dos pares é {somapar}.')
print(f'A soma da terceira coluna é {somacol}.')
print(f'O valor mais alto da segunda linha é {max(matriz[1])}')

#Ex 88: Faça um programa que ajude um jogador da Mega-Sena a criar palpites. O programa vai pergunrar quantos jogos serão
#gerados e vai criar 6 números de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
números = list(range(1, 61))
jogos = int(input('Quantos jogos serão jogados?'))
for c in range(1, jogos + 1):
        print(f'Os números do jogo {c} são {sample(números, k = 6)}')

#Ex 89: Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre
#um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
while True:
    nome = input('Nome:')
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    média = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], média])
    res = input('Quer continuar?[S/N]').upper()
    if res == 'N':
        break
for i, a in enumerate(alunos):
    print(f'{i} {a[0]} {a[2]}')
while True:
    opc = int(input('Mostrar nota de qual aluno?[999] para sair.'))
    if opc == 999:
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}.')






