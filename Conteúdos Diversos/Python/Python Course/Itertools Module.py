import itertools #Comando para importar as itertools
#Infinite Iterators
#Count
counter = itertools.count() #Funciona como um contador, entre parênteses será o número inicial, e aumentará em 1 após cada iteração
counter = itertools.count(2, 2) #O contador começará em 2 e pulará de 2 em 2 após cada loop, podem ser usados números decimais e negativos
for num in counter: #O contador aumentará após cada loop, caso não haja exceção, será um loop infinito
    if num < 10:
        print(num)
    else:
        break

#Cycle
counter = itertools.cycle([1, 2, 3]) #O contador fará um ciclo entre as variáveis dadas
for num in counter: #Caso não haja exceção será um loop infinito
    print(num)

#Repeat
counter = itertools.repeat(2)  #Repetirá infinitamente a variável entre parênteses
counter = itertools.repeat(2, 3) #Repetirá a variável pelo número de vezes que for mencionado(3 vezes)
for num in counter:
    print(num)

#Zip
data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data)) #A função zip junta duas variáveis dentro de uma lista, o elemento 0
print(daily_data)                               #de uma variável ficará junto com o elemento 0 de outra variável e assim por diante

#Combinatoric Iterators
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

#Combinations
result = itertools.combinations(letters, 2)     #Todas as combinações possíveis entre os elementos da variável letter, o número indica quantos
for item in result:                             #elementos serão usados, sem repetir os valores e sem se importar com a ordem (a,b seria o mesmo que b,a)
    print(item)

#Permutations
result = itertools.permutations(letters, 2)    #Todas as combinações possíveis entre os elementos da variável letter, o número indica quantos
for item in result:                            #elementos serão usados, sem repetir os valores mas se importando com a ordem (a,b seria diferente de b,a)
    print(item)

#Product
result = itertools.product(letters, repeat=4)  #Todas as combinações possíveis os elementos da variável letter, o repeat indica quantos
for item in result:                            #elementos serão usados, repetindo os valores e se importando com a ordem (a,b seria diferente de b,a)
    print(item)


#Combinations with Replacement
result = itertools.combinations_with_replacement(letters, 4) #Todas as combinações possíveis entre os elementos da variável, o número indica quantos elementos
for item in result:                                          #serão usados, repetindo os valores e sem se importar com a ordem (a,b seria o mesmo que b,a)
    print(item)

#Terminating Iterators
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

#Chain
combined = itertools.chain(letters, numbers)  #Faz uma iteração sobre todos os itens de diferentes listas, e os combina em
for item in combined:                         #uma única lista
    print(item)

#Islice
result = itertools.islice(numbers, 0, 4, 2) #Fatia uma variável, mostrando apenas os elementos indicados
for item in result:                         #Vai do elemento na posição 0 até o elemento na posição 4 pulando de 2 em 2
    print(item)

#Compress
letters = ['a', 'b', 'c', 'd']
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors) #Atribui um valor booleano a uma variável, para então retornar apenas os
for item in result:                             #valores que são True
    print(item)

#Filter and Filterfalse
def less_2 (n):     #Cria uma função que se o número for menor que 2 retorna True
    if n < 2:
        return True 
    return False
numbers = [0, 1, 2 , 3]
result = filter(less_2, numbers) #A função filter retorna apenas as variáveis que forem True na função
result = itertools.filterfalse(less_2, numbers) #Essa função por sua vez retorna apenas as variáveis que forem False
for item in result:
    print(result)

#Accumulate
result = itertools.accumulate(numbers) #Itera sobre uma lista de variáveis, retornando o valor acumulado delas depois
for item in result:                    #de cada iteração
    print(item)

