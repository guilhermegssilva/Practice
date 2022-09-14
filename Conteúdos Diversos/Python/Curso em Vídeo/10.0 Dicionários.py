dados = {'nome': 'Pedro', 'idade': 25} #Ao invés do indexador ser um número, ele passará a ser uma palavra
print(dados['nome']) #Escreve na tela o elemento da varíavel nome
print(dados['idade']) #Escreve na tela o elemento da varíavel idade
dados['sexo'] = 'M' #Adiciona o elemento sexo com o valor M ao final da lista  [Pedro, 25, M]
dados['nome'] = 'Leandro' #Substitui um valor da varíavel por outro
del dados['idade'] #Remove um elemento específico da lista
pessoas = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} e é do sexo {pessoas["sexo"]}.') #Print formatado de dicionários


filme = {'título': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
print(filme.values()) #Irá retornar todos os valores da varíavel filmes (Star Wars, 1977, George Lucas)
print(filme.keys()) #Irá retornar todos os indexadores da varíavel filmes (título, ano, diretor)
print(filme.items()) #Irá retornar todos os itens da varível filmes
for k, v in filme.items(): #Para cada chave e valor na variável filme
    print(f'O {k} é {v}')


locadora = []
filme1 = {'título': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}
filme2 = {'título': 'Avengers', 'ano': '2012', 'diretor': 'Josh Whedon'}
filme3 = {'título': 'Matrix', 'ano': '1999', 'diretor': 'Wachowsky'}
locadora.append(filme1) #(listas são identificadas por números)
locadora.append(filme2) #(listas são identificadas por números)
locadora.append(filme3) #(listas são identificadas por números)
print(locadora[0]['ano']) #Irá retornar o índice ano do elemento zero dentro da lista locadora (1977)
print(locadora[2]['título']) #Irá retornar o índice título do elemento 2 dentro da lista locadora (Matrix)


estado = {}
brasil = []
for c in range (0,3):
    estado['uf'] = input('Estado:')
    estado['sigla'] = input('Sigla:')
    brasil.append(estado.copy()) #Função para adicionar uma cópia da varíavel, quando dentro de um laço

for e in brasil: #Para cada estado dentro do dicionário na lista brasil
    for k, v in e.items(): #Para cada valor e chave dentro de cada dicionário
        print(f'O campo {k} tem valor {v}')








