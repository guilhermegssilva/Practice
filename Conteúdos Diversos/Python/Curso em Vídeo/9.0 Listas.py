friends = ['Kevin', 'Karen', 'Jim'] #[] servem para armazenar vários elementos numa mesma varíavel
friends[1] = 'Mike' #Substitui um elemento específico da lista por outro
print(friends[0]) #Mostra apenas o primeiro nome
print(friends[-1]) #Mostra apenas o último nome
print(friends[1:5]) #Mostra apenas os nomes do primeiro até o quarto

valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor'))) #Os valores digitados serão colocados dentro de uma lista

valores = list(range(4,11)) #Cria uma lista com valores que vão de 4 até 10
for c,v in enumerate(valores): #O c mostra cada posição do laço(1º,2º,3°) e o v mostra cada item da lista(4 até 11)
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')


friends_list = ['Kevin', 'James','Jim', 'Karen', 'Otto']
len(friends_list) #Mostra quantos elementos estão em uma lista
friends_list.extend(valores) #Junta uma lista com outra lista, a nova lista será colocada ao final da lista original
friends_list.append('Creed') #Adiciona um único elemento em uma lista já existente, este será colocado no final dela
friends_list.insert(3, 'Jean') #Adiciona um elemento em uma posição específica da lista
friends_list.remove('Kevin') #Remove um item específico da lista
friends_list.pop(3) #Remove um elemento específico da lista, pelo seu índice, em branco será o último item
friends_list.sort() #Organiza a lista em ordem alfabética, ou em ordem crescente no caso de números
friends_list.sort(reverse=True) #Organiza uma lista em ordem decrecente tanto para letras quanto para números
friends_list.reverse() #Reverte a ordem dos elementos de uma lista, os últimos se tornando os primeiros
friends2 = friends_list.copy() #Copia os elementos de uma lista para uma nova lista
friends_list.clear() #Limpa uma lista
print(friends_list.index('Otto')) #Indica em qual posição da lista está localizado o nome
print(friends_list.count('Jim')) #Retorna o número de vezes que tal nome aparece na lista


pessoas = [['Pedro', 25], ['Maria',19], ['João',32]] #Criação de uma lista dentro de outra
print(pessoas[0][0]) #Retornará o elemento 0 dentro do elemento 0 de uma lista (Pedro)
print(pessoas[1][1]) #Retornará o elemento 1 dentro do elemento 1 de uma lista (19)
print(pessoas[2][0]) #Retornará o elemento 0 dentro do elemento 2 de uma lista (João)
lista = [2, 5, 6, 8]
lista1.append(lista) #Adiciona uma lista dentro de outra, as mudanças feitas na primeira serão feitas também dentro da outra
lista1 = lista #Copia e conecta duas listas, as mudanças feitas em uma serão feitas na outra
lista1 = lista[:] #Copia duas listas, mudanças feitas em uma não alterarão a outra
lista1.append(lista[:]) #Adiciona uma lista dentro de outra, as mudanças feitas na primeira não serão feitas na segunda
lista1[2] = 8 #Altera o terceiro elemento de uma/ambas as listas

pessoas = []
dados = []
for c in range(0,3): #Laço for com uma lista que muda após cada repetição
    dados.append(input('Nome:'))
    dados.append(input('Idade:'))
    pessoas.append(dados[:]) #Coloca uma cópia da lista temporária na lista pessoas após cada repetição
    dados.clear() #Limpa a lista temporária após cada repetição
print(pessoas)

for c in pessoas: #Laço que verifica cada lista dentro da lista pessoas
    if c[1] >= 21: #Condição para cada segundo elemento da lista, dentro da lista pessoas
        print(f'{p0} é maior de idade.')
    else:
        print(f'{p0} é menor de idade.')

maior = 0
menor = 0
while True:
    if len(pessoas) == 0: #Se a lista estiver vazia o primeiro elemento dela será o menor e menor valor
        menor = c[1]
    if c[1] > maior: #Se a variável idade for maior que maior valor, ela se tornará o maior valor
        maior = c[1]
    if c[1] < menor: #Se a varíavel idade for menor que o menor valor, ela se tornará o menor valor
        menor = c[1]