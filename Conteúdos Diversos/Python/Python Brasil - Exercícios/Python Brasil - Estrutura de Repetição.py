#Ex 01: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.
nota = int(input('Digite a nota: '))
while nota > 10:
    nota = int(input('Digite a nota: '))

#Ex 02: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
#uma mensagem de erro e voltando a pedir as informações.
user = input('Informe seu nome de usuário: ')
senha = input('Informe a senha')
if user != senha:
    print('Cadastrado com sucesso!')
while user == senha:
    print('Seus dados de acesso não podem ser iguais.')
    user = input('Informe seu nome de usuário: ')
    senha = input('Informe a senha')
    if user != senha:
        print('Cadastrado com sucesso!')

#Ex 03: Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = input('Informe seu nome: ')
    if len(nome) > 3:
        print('Cadastrado com sucesso')
    else:
        while len(nome) < 3:
            nome = input('Informe seu nome: ')
        print('Cadastrado com sucesso')

    idade = int(input('Informe sua idade: '))
    if idade > 0 and idade < 150:
        print('Cadastrado com sucesso')
    else:
        while idade < 0 or idade > 150:
            idade = int(input('Informe sua idade: '))
        print('Cadastrado com sucesso')

    sexo = input('Informe seu sexo: ')
    if sexo in 'fm':
        print('Cadastrado com sucesso')
    else:
        while sexo not in 'fm':
            sexo = input('Informe seu sexo: ')
    print('Cadastrado com sucesso')

    estado_civil = input('Informe seu estado civil: ')
    if estado_civil in 'scv':
        print('Cadastrado com sucesso')
        break
    else:
        while estado_civil not in 'scv':
            estado_civil = input('Informe seu estado civil: ')
        print('Cadastrado com sucesso')
        break
print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nEstado civil: {estado_civil}')

#Ex 04: Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
#a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
#de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paísA = 120000
paísB = 120000
cont = 0
while paísA < paísB:
    paísA = paísA + (paísA * 0.03)
    paísB = paísB + (paísB * 0.015)
    cont = cont + 1
print(f'Foram {cont} anos para igualar')

#Ex 05: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide
#a entrada e permita repetir a operação.
while True:
    paísA = int(input('População do país A: '))
    paísB = int(input('População do país B: '))
    cont = 0
    while paísA < paísB:
        paísA = paísA + (paísA * 0.03)
        paísB = paísB + (paísB * 0.015)
        cont = cont + 1
    print(f'Foram {cont} anos para igualar')
    resposta = input('Quer continuar?').upper()
    if resposta == 'N':
        break
print('Volte sempre')

#Ex 06: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para
#que ele mostre os números um ao lado do outro.
for c in range(1, 21):
    print(c)
for c in range(1, 21):
    print(c, end=' ')

#Ex 07: Faça um programa que leia 5 números e informe o maior número.
n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))
n3 = int(input('Informe o 3º número: '))
n4 = int(input('Informe o 4º número: '))
n5 = int(input('Informe o 5º número: '))
print(f'O maior número é {max(n1, n2, n3, n3, n4, n5)}')

#Ex 08: Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
cont = 0
for c in range(1, 6):
    n = int(input('Informe um número: '))
    soma = n + soma
    cont = cont + 1
print(f'A soma dos números é {soma}.\nA média dos números é {soma/cont}')

#Ex 9: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for c in range(1,51):
    if c % 2 != 0:
        print(c, end=' ')

#Ex 10: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
#por eles.
n1 = int(input(f'Digite um número: '))
n2 = int(input('Digite outro número: '))
for c in range(n1 + 1, n2):
    print(c, end=' ')

#Ex 11: Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input(f'Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = 0
for c in range(n1 + 1, n2):
    print(c, end=' ')
    soma = soma + c
print()
print(f'A soma dos números é {soma}.')

#Ex 12: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
#deve informar de qual numero ele deseja ver a tabuada.
num = int(input('Qual o número deseja ver?'))
print(f'TABUADA DO {num}')
for c in range(1,11):
    print(f'{num}X{c} = {num*c}')

#Ex 13: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
potência = 1
for c in range(1, n2 + 1):
    potência = n1 * potência
print(f'A potência é {potência}.')

#Ex 14: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
#números impares.
par = 0
impar = 0
somapar = 0
somaimpar = 0
for c in range(1,11):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par = par + 1
        somapar = num + somapar
    else:
        impar = impar + 1
        somaimpar = num + somaimpar
print(f'Foram {par} números pares e {impar} números ímpares')
print(f'A soma dos pares foi {somapar} e a soma dos ímpares foi {somaimpar}')

#EX 17: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
num = int(input('Digite um número: '))
fat = 1
for c in range(1, num + 1):
    fat = fat * c
print(f'O fatorial de {num} é {fat}.')

#Ex 18: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
soma = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número: '))
    soma = soma + num
    if num > maior:
        maior = num
    if num < menor or menor == 0:
        menor = num
    resposta = input('Quer parar? ')
    if resposta == 'S':
        break
print(f'A soma é {soma}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

#EX 19: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
soma = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número: '))
    while num > 100 or num < 0:
        num = int(input('Digite um número:'))
    soma = soma + num
    if num > maior or maior == 0:
        maior = num
    if num < menor or menor == 0:
        menor = num
    resposta = input('Quer parar? ')
    if resposta == 'S':
        break

print(f'A soma é {soma}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

#Ex 20: Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
#fatorial a números inteiros positivos e menores que 16.
while True:
    num = int(input('Digite um número: '))
    while num > 16:
        num = int(input('Digite um número: '))
    fat = 1
    for c in range(1, num + 1):
        fat = fat * c
    print(f'O fatorial de {num} é {fat}.')
    resposta = input('Quer continuar?')
    if resposta == 'N':
        break

#Ex 21: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
totdiv = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(c, end=' ')
        totdiv = totdiv + 1
if totdiv == 2:
    print('É primo!')
else:
    print('Não é primo!')

#Ex 24: Faça um programa que calcule o mostre a média aritmética de N notas.
soma = 0
cont = 0
while True:
    nota = int(input('Insira a nota: '))
    soma = soma + nota
    cont = cont + 1
    resposta = input('Quer continuar?')
    if resposta == 'N':
        break
print(f'A soma das notas é {soma}.')
print(f'A média das notas é {soma/cont}')

#Ex 25: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
#turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = 0
cont = 0
while True:
    idade = int(input('Informe a sua idade: '))
    soma = soma + idade
    cont = cont + 1
    resposta = input('Quer continuar? ')
    if resposta == 'N':
        break
média = soma / cont
print(f'A média de idades é {média}')
if média < 26:
    print('A turma é jovem')
elif média < 60:
    print('A turma é adulta')
elif média > 60:
    print('A turma é idosa')

#Ex 26: Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
#votar e ao final mostrar o número de votos de cada candidato.
total = int(input('Informe o número toral de eleitores: '))
print(f'No total serão {total} eleitores')
candA = candB = candC = 0
for c in range(1, total + 1):
    voto = input(f'Insira seu voto eleitor {c}: ')
    if voto == 'A':
        candA = candA + 1
    elif voto == 'B':
        candB = candB + 1
    elif voto == 'C':
        candC = candC + 1
print(f'Foram {total} votos computados.')
print(f'O canditado A recebeu {candA} votos.\nO candidato B recebeu {candB} votos.\nO candidato C recebeu {candC} votos.')
if candA > candB and candA > candC:
    print('O vencedor foi o candidato A')
elif candB > candC and candB > candA:
    print('O vencedor é o canditado B')
elif candC > candA and candC > candB:
    print('O vencedor é o candidato C')

#Ex 27: Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
#de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turmas = int(input('Informe a quantidade de turmas: '))
soma = 0
for c in range(1, turmas + 1):
    alunos = int(input('Informe a quantidade de alunos: '))
    soma = soma + alunos
print(f'A média de alunos por turma é {soma/turmas}')