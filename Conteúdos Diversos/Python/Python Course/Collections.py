import collections #Comando para importar as collections

#Counter
letras = 'aaaabbbcc'
my_counter = collections.Counter(letras) #A função Counter exibe a quantidade dos diferentes elementos de uma variável
print(my_counter)
print(my_counter.most_common(2)) #Escreve qual o elemento mais comum da variável, o número modifica quantos elementos serão mostrados

#Defaultdict
d = collections.defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c']) #Ao se colocar uma variável que não existe, ele retorna o valor 0 ao invés de um Key Error, pode ser
              #modificado para criar uma lista mudando oque está entre parênteses

#Deque
d = collections.deque()
d.append(1) #Adiciona um valor ao final da sequência
d.append(2) #Adiciona um valor ao final da sequência
d.appendleft(3) #Adiciona um valor no começo da sequência
d.pop() #Remove um valor do final da sequência
d.clear() #Remove todos os valores da sequência
d.extendleft([4, 5, 6]) #Adiciona os valores no começo da sequência, começando pelo último (6, 5, 4)
d.rotate(1) #Rotaciona os elementos uma vez, o 1º se torna o segundo, o último se torna o primeiro etc...
d.rotate(-1) #Rotaciona todos os elementos mas para a direção oposta (esquerda)
print(d)

#ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
c = dict(collections.ChainMap(d2, d1)) #Une dois dicionários em uma única variável, separados por vírgula
print(c)