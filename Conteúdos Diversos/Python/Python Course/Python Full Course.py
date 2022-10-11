#STRING E NÚMEROS
nome = 'Ana  Banana'.split()
print(f'Seu primeiro nome é {nome[1][3]}') #Mostra a 4ª letra do 2º nome
phrase = 'Giraffe\' Academy'.lower() #\' para inserir aspas dentro de uma string
print(phrase + ' is cool')
print(phrase.index('c')) #Mostra em quantos caracteres tem a primeira ocorrência especificada
my_num = -5
print(abs(my_num)) #Valor absoluto de um número
print(pow(3, 2)) #Primeiro número é o usado e o segundo indica a que potência elevar
print(max(4, 6)) #Indica o valor mais alto dentre os estipulados
print(min(4, 6)) #Indica o valor mais baixo dentre os estipulados


#LISTAS
friends = ['Kevin', 'Karen', 'Jim'] #[] servem para armazenar vários elementos numa mesma varíavel
friends[1] = 'Mike' #Substitui um elemento específico da lista por outro
print(friends[0]) #Mostra apenas o primeiro nome
print(friends[-1]) #Mostra apenas o último nome
print(friends[1:5]) #Mostra apenas os nomes do primeiro até o quarto

a = [2, 5, 6, 8]
b = a #Copia e conecta duas listas, as mudanças feitas em uma serão feitas na outra
b = a[:] #Apenas copia duas listas, mudanças feitas em uma não alterarão a outra
b[2] = 8 #Altera o terceiro elemento de uma/ambas as listas

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


#FUNÇÕES
def say_hi(): #def cria uma função, essa serve para executar um ou vários comandos
    print('Hello World')
say_hi() #Uma vez que a função foi criada é só digitar seu nome seguido de ()

def say_ho(name, age): #Entre parênteses está um parâmetro para a função
    print(f'Hello {name}, you have {age}')
say_ho('Mike','35') #Quando a função for chamada deve ser colocado algo entre os parênteses
say_ho('Steve', '56')

nome = input('Qual o seu nome') #É possível atribuir varíaveis para uma função
idade = int(input('Qual a sua idade'))
def ola(nome,idade):
    print(f'Olá {nome}, você tem {idade} anos')
ola(nome,idade)

def cube(num):
    #print(num*num*num)
    return num*num*num
cube(2)


#MANIPULANDO ARQUIVOS
open('nome do arquivo seguido do seu formato') #Comando para se abrir arquivos
f = open('10.0 Dicionários.py') #Se o arquivo estiver no mesmo diretório do projeto apenas o comando com o nome bastará
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto.txt') #Caso o arquivo esteja em outro diretório deverá ser colocado seu caminho
print(f.read()) #Comando que irá mostrar o conteúdo do arquivo
print(f.read(100)) #Comando que irá mostrar os 100 primeiros caracteres do arquivo, usando o número como parâmetro
print(f.readline()) #Comando que irá mostrar apenas apenas a primeira linha do arquivo, se repetido, irá ler a segunda linha e assim por diante
print(f.readlines()) #Comando que colocará todas as linhas dentro de uma lista, cada linha terá um índice diferente
print(f.readlines()[1]) #Irá mostrar apenas o elemento da posição 1 da lista criada
for c in f: #Para cada linha(c) no arquivo(f)
    print(c)

f = open('C:/Users/guilh/Desktop/Novo Documento de Texto.txt', 'a') #A letra a(append) após a vírgula indica que será adicionado algo escrito no fim do arquivo
f.write('Carro - Modelo Vermelho') #A frase será adicionada no final do arquivo
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto.txt', 'w') #A letra w(write) após a vírgula indica que o que for escrito irá sobrescrever o conteúdo que já estava no arquivo
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto123.txt', 'w') #Caso o arquivo não exista será criado um novo arquivo com esse nome
f.close() #Comando para fechar o arquivo após o seu uso

#CLASSES E OBJETOS
class Estudante: #Define o nome da classe. A classe pode receber qualquer característica para moldá-la do jeito que quiser. O ideal é criar um arquivo separado do principal, contendo as classes a serem usadas
    def __init__(self, nome, nota, estaDependente, idade): #Entre parênteses será colocado todas as características do objeto que será criado. Essas, por sua vez estarão presentes em todos os objetos criados dentro dessa classe
        self.nome = nome        #Essas são as características que cada objeto dentro dessa classe terá
        self.nota = nota
        self.estaDependente = estaDependente
        self.idade = idade

from 'nome do arquivo' import Estudante   #O nome do arquivo será o arquivo em que estão as classes, e Estudante é o nome da classe em si
Estudante1 = Estudante('Pedro', 7.0, True, 22) #Comando que cria o objeto, entre parênteses estão as varíaveis que ele irá receber
Estudante2 = Estudante('Ana', 8.5, False, 19) #Todos os objetos dentro da classe terão as mesmas características
print(Estudante1.nome) #Escreverá a variável nome do objeto Estudante1
