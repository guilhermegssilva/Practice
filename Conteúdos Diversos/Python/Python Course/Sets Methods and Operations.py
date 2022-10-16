#Sets
s1 = set() #Comando para se criar um set vazio
s1 = set([1, 2, 3, 4, 5, 5]) #O set criado não permite duplicatas dentro dele, portanto elas não serão consideradas além disso, dígitos sempre serão ordenados
s2 = {9, 10, 11} #Um set também pode ser criado colocando os elementos entre colchetes
s1.add(6) #Adicionará o elemento entre parênteses ao final do set
s1.update([6, 7, 8]) #Adicionará vários elementos dentro de um set, os elementos devem ser passados em forma de lista
s1.update([6, 7, 8], s2) #É possível adicionar mais de uma lista, ou ainda outros sets em um set já existente
s1.remove(11) #Remove um elemento do set, caso o elemento não exista apresentará um erro
s1.discard(11) #Remove um elemento do set sem apresentar erro caso o elemento não exista


set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
set4 = set1.intersection(set2) #Retorna os valores que estão em set2 e set1
set5 = set1.intersection(set2, set3) #Retorna os valores que estão em set2
set6 = set1.difference(set2) #Retorna os valores que estejam em set1 mas não em set2
set7 = set3.difference(set1, set2) #Retorna os valores que estejam em set3 mas não em set1 e set2
set8 = set1.symmetric_difference(set2) #Retorna todos os valores que forem únicos entre o set1 e o set2
print(set8)