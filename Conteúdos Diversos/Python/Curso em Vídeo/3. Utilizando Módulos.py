from math import sqrt, ceil
import random
num = float(input('Digite um número'))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {ceil(raiz)}!')
print(f'A raiz de {num} é igual a {raiz:.1f}!')
print(f'A raiz de {num} é igual a {raiz}!')
num1 = random.random()
num = random.randint(1, 10)
print(num, num1)