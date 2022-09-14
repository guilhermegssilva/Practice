#Ex 90:Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final mostre o
#conteúdo da estrutura na tela.
estudante = {}
estudante['Aluno'] = input('Nome do aluno: ')
estudante['Média'] = int(input(f'Média de {estudante["Aluno"]}: '))
if estudante['Média'] >= 7:
    estudante['Situação'] = 'Aprovado'
else:
    estudante['Situação'] = 'Reprovado'
for k, v in estudante.items():
    print(f'{k} é igual a {v}')

#Ex 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final coloque esse dicionário em ordem sabendo que o vencedor foi aquele que tirou o maior número.
from random import randint
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores Sorteados:')
for k,v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
ranking = []
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

#Ex 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se a CTPS for diferente de zero, o dicionário receberá tembém o ano de contratação e o salário. Calcule e acrescente além
# da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
pessoa = {}
pessoa['Nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - nascimento
pessoa['CTPS'] = int(input('Nº carteira de trabalho:[0] caso não tenha. '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Ano de contratação'] + 40
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')

#Ex 93:Crie um programa que gerencie o aproveitamento de um jogo de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidade de gols feita em cada partida. No final tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
jogador['nome'] = input('Nome: ')
jogador['gols'] = int(input('Nº partidas: '))
for c in range(1, jogador['gols'] + 1):
    gols.append(int(input(f'Quantos gols na partida {c} ')))
jogador['total de gols'] = sum(gols)
jogador['gols'] = gols
print(jogador)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for c,v in enumerate(gols):
    print(f'Na partida {c + 1} foram {v} gols')
print(f'Foi um total de {sum(gols)} gols.')

#Ex 94: Crie um programa que leia o nome, idade e sexo de várias pessoas. Guardando os dados de cada pessoa em um dicionário
#e todos os dicionários em uma lista. No final mostre: Quantas pessoas foram cadastradas, a média de idade do grupo, uma lista
#com todas as mulheres, uma lista com todas as pessoas com idade acima da média.
pessoas = []
dados = {}
idades = []
while True:
    dados.clear()
    dados['Nome'] = input('Nome: ')
    dados['Idade'] = int(input('Idade: '))
    idades.append(dados['Idade'])
    dados['Sexo'] = input('Sexo: ').upper()
    pessoas.append(dados.copy())
    resposta = input('Quer continuar?[S/N] ')
    if resposta in 'Nn':
        break
médiaidades = sum(idades) / len(idades)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idades é {médiaidades:.1f}.')
print(f'As mulheres cadastradas foram', end=' ')
for c in pessoas:
    if c['Sexo'] == 'F':
        print(f'{c["Nome"]}')
print()
for c in pessoas:
    if c['Idade'] > médiaidades:
        print(f'Acima da média estão {c["Nome"]}')

#Ex 95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
#de aproveitamento de cada jogador.
dado=dict()
t=[]
w=[]
n=[]
while True:
    dado.clear()
    dado["nome"]=str(input('digite o nome do jogador: '))
    j=int(input('quantas partidas o {} jogo?: '.format(dado["nome"])))
    n.clear()
    for i in range(j):
        n.append(int(input('quantos gols foi feito na partida {}: '.format(i))))
    dado["gols"] = n[:]
    dado["total"] = sum(n)
    w.append(dado.copy())
    n2=str(input("quer continuar?")).upper().strip()[0]
    while n2 not in "NnSs":
          print('resposta invalida,digite novamnete ')
          n2=str(input("quer continuar?")).upper().strip()[0]
    if n2 in "Nn":
        break
print('',end='')
for i in dado.keys():
    print('{:<15}'.format(i), end=' ')
print()
for k,v in enumerate(w):
    print('{:>2} '.format(k), end='')
    for d in v.values():
        print('{:<15}'.format(str(d)),end=' ')
    print()
while True:
    n3=int(input('digite o numero do jogador,(999 para sair): '))
    if n3 == 999:
        break
    if n3>len(w):
        print('não tem esse numero')
    for h,q in enumerate(w):
        if h==n3:
            print('levatamento dos do jogador {}'.format(h))
            print('nome:{} '.format(h,q["nome"]))
