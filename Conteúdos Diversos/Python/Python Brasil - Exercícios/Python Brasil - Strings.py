#Ex 01: Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
frase1 = input('Digite a 1º frase: ')
frase2 = input('Digite a 2º frase: ')
print(f'A frase "{frase1}" possui {len(frase1)} caracteres')
print(f'A frase "{frase2}" possui {len(frase2)} caracteres')
if len(frase1) == len(frase2):
    print('As duas frases têm o mesmo tamanho', end=' ')
    if frase1 == frase2:
        print('e possuem o mesmo conteúdo.')
    else:
        print('mas não possuem o mesmo conteúdo.')

else:
    print('As duas frases não têm o mesmo tamanho', end=' ')
    if frase1 == frase2:
        print('mas possuem o mesmo conteúdo.')
    else:
        print('e não possuem o mesmo conteúdo.')

#Ex 02:Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
#utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
nome = input('Digite o seu nome: ').upper()
print(f'O seu nome em maiúsculo ao contrário fica {nome[::-1]}')

#Ex 03: Faça um programa que solicite o nome do usuário e imprima-o na vertical.
nome = input('Digite o seu nome: ')
for c in nome:
    print(f'{c}')

#Ex 04: Modifique o programa anterior de forma a mostrar o nome em formato de escada.
nome = input('Digite o seu nome: ')
lista = []
for c in nome:
    lista.append(c)
    print(''.join(lista))

#Ex 05: Altere o programa anterior de modo que a escada seja invertida.
nome = input('Digite o seu nome: ')
nomeInverso = nome[::-1]
lista = []
for c in nomeInverso:
    lista.append(c)
    print(''.join(lista))
#Ex 06: Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
data = input('Em que ano você nasceu?')
meses = {'1': 'janeiro', '2': 'fevereiro', '3': 'março', '4': 'abril', '5': 'maio', '6': 'junho', '7': 'julho', '8': 'agosto',
        '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
lista = data.split('/')
print(f'Você nasceu no dia {lista[0]} de {meses[lista[1]]} do ano {lista[2]}')

#Ex 07: Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#Quantos espaços em branco existem na frase.
#Quantas vezes aparecem as vogais a, e, i, o, u.
frase = input('Digite uma frase:').lower()
print(f'A frase possui {frase.count(" ")} espaços em branco.')
print(f'''VOGAIS:
a: {frase.count('a')}
e: {frase.count('e')}
i: {frase.count('i')}
o: {frase.count('o')}
u: {frase.count('u')}''')

#Ex 08: Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
frase = input('Digite uma frase: ').strip()
frase = frase.replace(' ', '')
fraseInversa = frase[::-1]
if frase == fraseInversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

#Ex 09: Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um
#número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
num = input('Digite seu CPF: ')
num1 = num.replace('-', '.').split('.')
if len(num1[0]) == 3 and len(num1[1]) == 3 and len(num1[2]) == 3 and len(num1[3]) == 2:
    print('É válido!')
else:
    print('Não é válido!')

#Ex 10: Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
num = int(input('Digite um número: '))
lista = []
unidade = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'}
dezena = {2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta', 7: 'setenta', 8: 'oitenta', 9: 'noventa'}
for c in str(num):
    lista.append(int(c))
if num < 20:
    print(f'O número digitado é {unidade[num]}.')
elif lista[1] == 0:
    print(f'O númmero digitado é {dezena[lista[0]]}')
elif lista[1] != 0:
    print(f'O número digitado é {dezena[lista[0]]} e {unidade[lista[1]]}')

#Ex 11 :Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
#O jogador poderá errar 6 vezes antes de ser enforcado.
from random import choice
print('JOGO DA FORCA')
print()

palavras = ['arvore', 'estudante', 'python', 'viajar', 'jabuticaba', 'caramelo', 'escola', 'atletismo']
palavra = list(choice(palavras))
oculto = list('_' * len(palavra))
cont = 0
while True:
    palpite = input('Escolha uma letra ')
    cont = cont + 1
    for c, l in enumerate(palavra):
        if palpite == palavra[c]:
            oculto[c] = palpite
    print(' '.join(oculto))
    print()
    if oculto == palavra:
        break
print(f'Parabéns, você acertou a palavra. Foram necessárias {cont} tentativas.')

#Ex 12: Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 8 dígitos, acrescentando
#o '9' na frente. O usuário pode informar o número com ou sem o traço separador.
num = input('Digite o número de telefone: ')
num = num.replace('-', '')
if len(num) <= 8:
    print('O número digitado possui 8 dígitos. Será acrescentado o número 9')
    print(f'O número de telefone será 9{num[:4]}-{num[4:]}')

#Ex 13: Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas
#para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
from random import choice, sample
cont = 1
listaPalavras = ['arvore', 'caramelo', 'estudante', 'viajar', 'jabuticaba', 'penhorar']
palavra = choice(listaPalavras)
palavraEmbar = (''.join(sample(palavra, len(palavra))))
print(f'A palavra embaralhada é < {palavraEmbar} >')
while True:
    resposta = input('Sua resposta: ')
    if resposta == palavra:
        print('Parabéns você venceu!!')
        print(f'Você precisou de {cont} tentativas.')
        break
    else:
        print('Essa não é a resposta certa.')
        print('Tente de novo')
        cont = cont + 1
print('Obrigado por jogar')
