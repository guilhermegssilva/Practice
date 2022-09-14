#Ex 46: Faça um programa que mostre na tela uma contagem regressiva, de 10 a 0 com pausa de 1 segundo.

from time import sleep
for c in range(10,0,-1):
    print(f'{c:=^5}')
    sleep(1)

#Ex 47: Crie um programa que mostre na tela todos os números pares entre 0 e 50.

for c in range(0,52,2):
    print(c)

#Ex 48: Faça um programa que calcule a soma entre todos os números ímpares, múltiplos de três entre 1 e 500.
s = 0
cont = 0
for c in range(1,501):
    if (c % 2) != 0 and (c % 3) == 0:
        s=c+s
        cont = cont+1
print(f'A soma dos {cont} números será {s}')

s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s=s+c
        cont=cont+1
print(f'A soma dos {cont} será {s}')

#Ex 49: Faça um programa que mostre a tabuada de um número.
num = int(input('Digite um número'))
for c in range(1,11):
    print(f'{num} * {c} será {num*c}')

#Ex 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
s = 0
for c in range(0,6):
    n = float(input('Digite um número'))
    if (n % 2) == 0:
        s=n+s
print(f'A soma dos números pares será {s}')

#Ex 51: Faça um programa que leia o primeiro termo e a razão de uma PA. Após isso mostre os primeiros 10 números.

primeiro = int(input('Primeiro termo'))
razão = int(input('Razão'))
décimo = primeiro + (10-1) * razão
for c in range(primeiro,décimo+razão,razão):
    print(c,end=' ')

#Ex 52: Crie um programa que leia um número e diga se ele é ou não primo.
num = int(input('Digite um número'))
tot = 0
for c in range(1,num+1):
    if num%c==0:
        tot=tot+1
print(f'O número {num} foi divisível {tot} vezes')
if tot==2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')

#Ex 53: Crie um programa que leia uma frase e diga se ela é ou não um palíndromo. Desconsidere espaços.
frase = input('Digite uma frase').lower().replace(' ','').strip()
if frase==(frase[::-1]):
    print('É um palindromo')
else:
    print('Não é um palíndromo')

#Ex 54: Crie um programa que leia a data de nascimento de sete pessoas e diga quantas delas não atingiram maioridade.
from datetime import datetime
data = datetime.now().year
cont = 0
contm = 0
for pess in range(1,8):
    ano = int(input(f'Digite o anos que a {pess}ª pessoa nasceu.'))
    if (data-ano)>=18:
        cont = cont+ 1
    else:
        contm = contm + 1
print(f'{cont} pessoas são de maior e {contm} não são.')

#Ex 55: Faça um programa que leia o peso de cinco pessoas. No final mostre o maior e menor pesos entre elas.
pesos = []
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print(f'O maior peso é {max(pesos)}Kg')
print(f'O menor peso é {min(pesos)}Kg')

#Ex 56: Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. Depois mostre a média de idade
#do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total = 0
mul = 0
maioridade = 0
nomevelho = ''
for c in range(1,5):
    nome = input(f'Qual o nome da {c}ª pessoa?')
    idade = int(input(f'Qual a idade da {c}ª pessoa?'))
    sexo = (input(f'Qual o sexo da {c}ª pessoa?[M/F]')).upper().strip()
    total = idade+total
    if c == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and maioridade < idade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade<20:
        mul = mul+1
print(f'O homem mais velho tem {maioridade} e se chama {nomevelho}.')
print(f'{mul} mulheres têm menos de 20 anos.')
média = total/4
print(f'A média de idade do grupo é {média}.')








