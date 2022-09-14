lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim') #[0, 1, 2, 3], tuplas são escritas entre parênteses
print(lanche[1]) #Irá mostrar o primeiro elemento da tupla
print(lanche[-2]) #Irá mostrar o segundo elemento de trás para frente
print(lanche[1:3]) #Irá mostrar do primeiro elemento até o segundo
print(lanche[2:]) #Irá mostrar do segundo elemento até o final
print(lanche[:2]) #Irá mostrar do começo até o elemento primeiro elemento
print(lanche[-2:]) #Irá mostrar do segundo elemento de trás para frente até o final
print(len(lanche)) #Irá mostrar quantos elementos existem na varíalvel lanche, começando do um
print(sorted(lanche)) #Irá mostrar os itens da varíavel lanche em ordem alfabética
del(lanche) #Irá apagar totalmente uma tupla

for c in lanche: #Inicia uma repetição com cada um dos itens da tupla. Nesse caso o c corresponde a cada um dos itens
    print(f'Eu vou comer {c}')

for c in range (0, len(lanche)): #Inicia uma repetição do 0 até o número de itens da varíavel lanche
    print(f'Eu vou comer {lanche[c]}') #Escreve cada um dos elementos da varíavel lanche

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Irá juntar as duas tuplas em uma só, começando pela a seguida pela b
print(c.count(5)) #Irá mostrar quantas vezes aparece o número 5 na tupla
print(c.index(8)) #Irá mostrar em que posição da tupla está o número 8, começando do zero