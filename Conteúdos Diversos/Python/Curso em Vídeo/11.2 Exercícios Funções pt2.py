#Ex 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
#e, retornando um valor literal dizendo se uma pessoa tem voto obrigatório, opcional ou negado nas eleições.
from datetime import datetime
def voto(age):
    if idade >= 60:
        print(f'Com {idade} anos o voto é opcional.')
    if idade < 60:
        print(f'Com {idade} anos o voto é obrigatório.')
    if idade < 16:
        print(f'Com {idade} anos o voto é negado.')

nasc = int(input('Em que ano você nasceu?'))
idade = datetime.now().year - nasc
voto(nasc)

#Ex 102: Crie um programa que tenha uma função fatorial() que receba dois parãmetro, o primeiro será o número a ser calculado
#e o segundo será chamado show indicando se deverá ou não ser indicado o processo de cálculo do fatorial.
def fatorial(num = 1, show = bool):
    f=1
    for a in range(num, 0, -1):
        f = f * a
    if show == True:
        for b in range(num, 1, -1):
            print(f'{b} x', end=' ')
        return f'1 = {f}'
    else:
        return f

print(fatorial(5, show=True))

#Ex 103: Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros, o nome do jogador e a quantidade de
#gols que ele marcou. O programa deverá ser capaz de informar a ficha do jogador mesmo que algum dado não tenha sido informado
#corretamente.
def ficha(nome = 'desconhecido', gol = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = '0'
    return f'O jogador {nome} fez {gol} gols no campeonato'

jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
print(ficha(jogador, gols))

#Ex 104: Crie um programa que tenha a função leiaInt(), que vai funcionar semelhante a função input(), mas fazendo a validação
#para aceitar apenas valores numéricos.
def leiaint():
    while True:
        n = str(input("Digite um valor numerico: "))
        if n.isnumeric():
            n = int(n)
            break
    print(f'Voce digitou o Numero {n}')

leiaint()

#Ex 105: Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e retornar um dicionário
#com as seguintes informações: Quantidade de notas, a maior nota, a menor nota e a média da turma.
def notas(*num):
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    return r

print(notas(1, 2, 3, 4, 5))
