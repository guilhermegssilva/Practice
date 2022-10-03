#Lendo em Arquivos
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

#Escrevendo em Arquivos
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto.txt', 'a') #A letra a(append) após a vírgula indica que será adicionado algo escrito no fim do arquivo
f.write('Carro - Modelo Vermelho') #A frase será adicionada no final do arquivo, desde que o arquivo esteja aberto em modo append
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto.txt', 'w') #A letra w(write) após a vírgula indica que o que for escrito irá sobrescrever o conteúdo que já estava no arquivo
f = open('C:/Users/guilh/Desktop/Novo Documento de Texto123.txt', 'w') #Caso o arquivo não exista será criado um novo arquivo com esse nome
f.close() #Comando para fechar o arquivo após o seu uso


with open('Novo Documento de Texto.txt', 'r') as f: #Outra forma de se abrir um arquivo, o código fica identado, e não é necessário fechar o arquivo após o uso
    pass  #Aqui será escrito o código para manipular o arquivo, ele ficará identado
