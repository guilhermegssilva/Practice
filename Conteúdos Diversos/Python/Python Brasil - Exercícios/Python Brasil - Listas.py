#Ex 01: Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
lista = []
for c in range(5):
    lista.append(int(input('Digite um número: ')))
print(lista)

#Ex 02: Faça um programa que leia um vetor de 5 números reais e mostre-os na ordem inversa.
lista = []
for c in range(5):
    lista.append(int(input('Digite um número: ')))
lista.reverse()
print(lista)

#Ex 04: Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista = ['a', 'v', 'i', 'q', 't', 'h', 'o', 'x', 'b', 'd']
for c in lista:
    if c in 'aeiou':
        print(c, end=', ')

#Ex 05: Faça um programa que leia 6 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
#números IMPARES no vetor impar. Imprima os três vetores.
lista = []
listapar = []
listaimpar = []
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
print(f'Os números digitados foram {lista}.')
print(f'Os números pares são {listapar}.\nOs números ímpares são {listaimpar}.')

#Ex 06:Faça um programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada aluno, imprima
#o número de alunos com média maior ou igual a 7.0.
notas = []
for a in range(4):
    notas.append([])
    print(f'Digite as notas do {a+1}º aluno: ')
    for n in range(1,5):
        notas[a].append(int(input(f'Digite a nota: ')))
cont = 0
for c in range(0,4):
    média = sum(notas[c]) / len(notas[c])
    if média > 7:
        cont = cont + 1
print(f'Foram {cont} alunos aprovados!')

#Ex 07: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
for c in range(1,6):
    lista.append(int(input('Digite um número: ')))
print(f'Os números foram {lista}.')
print(f'A soma dos números é {sum(lista)}')
mult = 1
for c in lista:
    mult = mult * a
print(f'A multiplicação dos números é {mult}')

#Ex 08: Faça um programa que peça a idade e a altura de 3 pessoas, armazene cada informação no seu respectivo vetor. Imprima
#a idade e a altura na ordem inversa a ordem lida.
alturas = []
idades = []
for c in range(1,4):
    alturas.append(int(input('Digite sua altura em cm: ')))
    idades.append(int(input('Digite sua idade: ')))

print(f'A ordem inversa de idades é {sorted(idades, reverse=True)}')
print(f'A ordem inversa de alturas é {sorted(alturas, reverse=True)}')

#Ex 09: Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
números = []
for c in range(1,11):
    números.append(int(input('Digite um número: ')))
somapot = 0
for n in números:
    pot = n * n
    somapot = pot + somapot
print(f'A soma das potências é {somapot}.')

#Ex 11: Foram anotadas as idades e alturas de 30 alunos. Faça um programa que determine quantos alunos com mais de 13 anos
#possuem altura inferior à média de altura desses alunos.
cont = 0
média_altura = soma_altura / num_alunos
if idade > 13 and altura < média_altura:
    cont = cont + 1
print(f'{cont} alunos com mais de 13 anos estão abaixo da média de altura.')

#Ex 13: Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média
#anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram.
meses = [['Janeiro'], ['Fevereiro'], ['Março'], ['Abril'], ['Maio'], ['Junho'], ['Julho'], ['Agosto'],
['Setembro'], ['Outubro'], ['Novembro'], ['Dezembro']]
soma_temp = 0
for c, m in enumerate(meses):
    temp = int(input(f'Insira a temperatura média do mês de {m}: '))
    meses[c].append(temp)
    soma_temp = soma_temp + temp
média_temp = soma_temp / len(meses)
print(f'A média de temperatura no ano foi {média_temp:.1f}')
print(f'Os meses que estiveram acima da média foram')
for x in meses:
    if x[1] > média_temp:
        print(x[0])

#Ex 15: Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
#quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
lista = []
num = 0
while num != -1:
    num = int(input('Digite um número: '))
    lista.append(num)
lista.pop()
print(f'Foram lidos {len(lista)} valores.')
print(f'Os valores lidos foram', end=' ')
for c in lista:
    print(c, end=' ')
print()
print(f'Os valores lidos de forma inversa são {sorted(lista, reverse=True)}.')
print(f'A soma dos valores foi {sum(lista)}.')
print(f'A média dos valores foi {sum(lista)/len(lista)}.')
média = sum(lista) / len(lista)
print(f'Os valores acima da média são', end=' ')
for c in lista:
    if c > média:
        print(c, end=' ')
print()
print('Os valores abaixo de sete são:')
for c in lista:
    if c < 7:
        print(c)
print('Acabou!!!')

#Ex 17: Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
#pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
#atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
saltos = []
while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    for c in range(1,6):
        saltos.append(float(input(f'Digite a distância do {c}º salto: ')))
    print(f'Atleta: {nome}')
    print()
    for c, s in enumerate(saltos):
        print(f'{c+1}º salto: {s}m')
    print()
    média = sum(saltos) / len(saltos)
    print('Resultado Final')
    print(f'Atleta: {nome}')
    print(f'Saltos: {saltos[0]}m-{saltos[1]}m-{saltos[2]}m-{saltos[3]}m-{saltos[4]}m')
    print(f'Média dos saltos: {média:.1f}m')
    saltos.clear()
print('Acabou')

#Ex 24: Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
#Depois, mostre quantas vezes cada valor foi conseguido.
from random import randint
jogadas = []
for c in range(1, 101):
    num = randint(1, 6)
    jogadas.append(num)
print(jogadas)
for c in range(1, 7):
    print(f'O número {c} foi jogado {jogadas.count(c)} vezes.')