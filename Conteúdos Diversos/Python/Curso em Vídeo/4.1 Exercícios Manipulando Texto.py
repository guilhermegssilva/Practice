#Ex 22: Crie um programa que leia o nome completo de uma pessoa e mostre seu nome com letras maiúsculas,minúsculas
#total de letras no nome(sem espaços) e o número de letras no primeiro nome.
nome = input('Qual o seu nome?').strip()
print(f'O seu nome em maiúsculo fica {nome.upper()} \nO seu nome em minúsculo fica {nome.lower()}')
print('O número de total letras no seu nome é {}'.format(len(nome)-nome.count(' ')))
nome2 = len(nome)-nome.count(' ')
print(f'O número total de letras no seu nome é {nome2}')
dividido = nome.split()
print(f'O seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras')

#Ex 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um número'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade {u}\nDezena {d}\nCentena {c}\nMilhar {m}')

#Ex 24: Crie um programa que leia o nome de uma cidade e diga se ela começa com Santo.
nome = input('Diga o nome de uma cidade').strip()
print(nome[:5].upper() == 'SANTO ')

#Ex 25: Desenvolva um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.
nome = input('Qual o seu nome?')#.upper()
print(' SILVA ' in nome.upper())

#Ex 26: Faça um programa que leia uma frase e mostre quantas vezes aparece a letra 'A' e em que posição
#ela aparece pela primeira e pela última vez.
frase = input('Digite uma frase').upper()
print(f'Vezes que aparece a letra A {frase.count("A")}')
print(f'A primeira vez que o A aparece foi em {frase.find("A")}')
print(f'A última vez que o a aparece foi em {frase.rfind("A")}')

#Ex 27: Faça um programa que leia o nome de uma pessoa e em seguida mostre o primeiro e último nome separadamente.
nome = input('Digite seu nome').split()
print(f'Primeiro nome:{nome[0]}\nÚltimo nome:{nome[-1]}')









