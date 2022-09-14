#Ex 16: Crie um programa que leia um número e mostre na tela sua porção inteira.
from math import trunc
num = float(input('Digite um número'))
print(f'{num} inteiro é {trunc(num)}')

#Ex 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#e depois calcule e mostre a sua hipotenusa.
from math import sqrt
from math import hypot
cat1 = int(input('Qual o comprimento do 1º cateto?'))
cat2 = int(input('Qual o comprimento do 2º cateto?'))
hip = (pow(cat1,2) + pow(cat2,2))
hipf = sqrt(hip)
print(f'A hipotenusa é {hipf:.3}')
hip = hypot(cat1,cat2)
print(f'A hipotenusa é {hip:.2}!')

#Ex 18: Desenvolva um programa que leia um ângulo qualquer e mostre seu seno, coseno e tangente.
from math import cos,tan,radians,sin
ângulo = float(input('Digite o ângulo'))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o Seno de {seno:.2}, o coseno de {coseno:.2} e a tangente de {tangente:.2}')

#Ex 19: Faça um programa que leia o nome de quatro alunos e sorteie um deles.
from random import choice
aluno1 = str(input('Qual o nome do aluno?'))
aluno2 = str(input('Qual o nome do aluno?'))
aluno3 = str(input('Qual o nome do aluno'))
aluno4 = str(input('Qual o nome do aluno'))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}!')

#Ex 20: Faça um programa que leia o nome de quatro alunos e ordene-os aleatoriamente.
from random import shuffle
n1 = str(input('Primeiro aluno'))
n2 = str(input('Segundo aluno'))
n3 = str(input('Terceiro aluno'))
n4 = str(input('Terceiro aluno'))
lista = [n1,n2,n3,n4]
shuffle(lista)
print(f'A ordem será {lista}')










