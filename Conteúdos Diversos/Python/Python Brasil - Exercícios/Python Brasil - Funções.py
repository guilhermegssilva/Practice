#Ex 01: Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3
# n n n n n n ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def imprimir(num):
    for c in range(1, num + 1):
        print(f'{c} ' * c)
imprimir(4)

#Ex 02: Faça um programa para imprimir:
# 1
# 1 2
# 1 2 3
# 1 2 3 ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
lista = []
def nesima(num):
    for c in range(1, num + 1):
        lista.append(c)
        print(' '.join(str(e) for e in lista))
nesima(4)

#Ex 03: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(a, b, c):
    print(a + b + c)
soma(1, 2, 3)

#Ex 04: Faça um programa com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’ se seu
#argumento for positivo, e ‘N’ se seu argumento for zero ou negativo.
def posneg(num):
    if num <= 0:
        print('N')
    else:
        print('P')
posneg(8)

#Ex 05: Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
#quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera”
#o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto, custo):
    taxaImposto = taxaImposto / 100
    print(custo + (custo * taxaImposto))
somaImposto(5, 100)

#Ex 07: Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função
#valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir
#o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que
#seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
#que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para
#pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valorPagamento(valor, atraso):
    if atraso == 0:
        multa = 0
    else:
        multa = ((0.1 * atraso) + 3) / 100
    print(f'Com {atraso} dias de atraso a multa será de R${multa * 100:.2f}')
    print(f'O valor a ser pago será R${valor + (valor * multa):.2f}')
valorPrestação = []
quantPrestação = []
while True:
    valor = float(input('Digite o valor a ser pago: '))
    if valor == 0:
        break
    atraso = int(input('Digite os dias de atraso: '))
    valorPagamento(valor, atraso)
    valorPrestação.append(valor + (valor * ((0.1 * atraso) + 3) / 100))
    quantPrestação.append(atraso)
print(f'No total foram pagas {sum(quantPrestação)} prestações.\nNo total o valor pago foi R${sum(valorPrestação):.2f}')

#Ex 08: Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def tamanho(num):
    print(f'Essa número tem {len(str((num)))} dígitos.')
tamanho(1254588)

#Ex 09: Faça uma função que retorne o reverso de um número inteiro informado.
def inverso(num):
    print(str(num)[::-1])
inverso(876)

#Ex 10: Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
#Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é
#chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo
#agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar
#este Ponto novamente.
from random import randint
from time import sleep
lista = []
cont = 1
while True:
    print(f'RODADA {cont}:')
    sleep(1)
    jogada = randint(2, 12)
    if cont == 1 and jogada == 7 or jogada == 11:
        print(f'Sua jogada foi {jogada}\nVocê é um natural\nVocê ganhou')
        sleep(1)
        break
    elif cont == 1 and jogada == 2 or jogada == 3 or jogada ==12:
        print(f'Sua jogada foi {jogada}\nÉ um Craps\nVocê perdeu')
        sleep(1)
        break
    else:
        print(f'Sua jogada foi {jogada}')
        if cont > 1 and jogada == 7:
            print('Você perdeu')
            break
        lista.append(jogada)
    cont = cont + 1
    if lista.count(jogada) == 2:
        print(f'Você jogou o número {jogada} pela segunda vez\nVocê ganhou')
        break
print('OBRIGADO POR JOGAR')


#Ex 11: Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
def dataExtenso(data):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
             ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
             ['outubro', 31], ['novembro', 30], ['dezembro', 31]]

    data = data.split('/')
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('Data inválida')

def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28

dataExtenso('06/05/2020')


#Ex 12: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo:
#se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória.
#Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
from random import shuffle
def embaralha(mensagem):
    lista = []
    palavra = mensagem.upper()
    for c in palavra:
        lista.append(c)
    shuffle(lista)
    print(''.join(lista))
embaralha('arvore')