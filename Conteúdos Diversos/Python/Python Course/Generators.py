#Generators
#Generators são usados quando não é necessário saber os elementos anteriores ou posteriores da iteração
#Por estarem somente mostrando cada elemento individualmente o processo é muito mais rápido, uma vez que o elemento é mostrado, ele será descartado e a sequencia seguirá
#Um exemplo é procurar uma palavra específica em um texto, onde o único elemento que importa é a palavra em si
from time import process_time

t1_start = process_time()

x = [i**2 for i in range(10000)] #Todos os números ficam armazenados na memória, resultando em um processo mais lento
for el in x:
    print(el)

for c in range(10000): #Todos os números ficam armazenados na memória, resultando em um processo mais lento
    print(c**2)

t1stop = process_time()
print(t1stop - t1_start, 'seconds')

#####################################

t2_start = process_time()

def gen(n): #Função que cria um generator, uma vez que o comando yield está presente ela se torna um generator
    for i in range(n):
        yield i**2   #O método yield cria um generator contendo os resultados de i**2

g = gen(10000)  #A variável g recebe esse generator que contém os resultados
for c in g: #Para cada número na variável g
    print(c)

t2stop = process_time()
print(t2stop - t2_start, 'seconds')