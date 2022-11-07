#Ex 01: Faça um programa que peça dois número e imprima o maior deles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print(f'Entre os números {n1} e {n2}:')
if n1 > n2:
    print(f'{n1} é o maior número.')
elif n1 == n2:
    print(f'{n2} e {n1} são iguais.')
elif n1 < n2:
    print(f'{n2} é o maior número.')

#Ex 02: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = int(input('Digite um valor:'))
if n < 0:
    print(f'O valor {n} é negativo.')
else:
    print(f'O valor {n} é positivo')

#Ex 03: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite seu sexo: [M/F]').upper()
if sexo == 'F':
    print('Seu sexo é feminino')
elif sexo == 'M':
    print(f'Seu sexo é masculino')
elif sexo not in 'MF':
    print('Sexo inválido')

#Ex 04: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ').upper()
if letra not in 'AEIOU':
    print(f'A letra {letra} é consoante')
else:
    print(f'A letra {letra} é vogal')

#Ex 05: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média == 10:
    print(f'Com a média {média} você está aprovado com distinção.')
elif média >= 7:
    print(f'Com a média {média} você está aprovado.')
elif média < 7:
    print(f'Com a média {média} você está reprovado.')

#Ex 06: Faça um programa que leia três números e mostre o maior deles.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
print(f'O maior número é {max(n1, n2, n3)}.')

#Ex 07: Faça um programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
print(f'O maior número é {min(n1, n2, n3)}.')

#Ex 08: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.
n1 = float(input('Digite o preço do 1º produto: '))
n2 = float(input('Digite o preço do 2º produto: '))
n3 = float(input('Digite o preço do 3º produto: '))
print(f'O produto a ser comprado é o que custa {min(n1, n2, n3)}.')

#Ex 09: Faça um programa que leia três números e mostre-os em ordem decrescente.
lista = []
for c in range(0,3):
    lista.append(int(input('Digite um número: ')))
nlista = sorted(lista,reverse=True)
print(*nlista, sep=", ")

#Ex 10: Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = input('Qual turno você estuda? [M/V/N]').upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
elif turno not in 'MVN':
    print('Opção inválida')

#Ex 11: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#Salários até R$ 280,00 (incluindo) : aumento de 20%
#Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#Salários de R$ 1500,00 em diante : aumento de 5%. Após o aumento ser realizado, informe na tela:
#O salário antes do reajuste;
#O percentual de aumento aplicado;
#O valor do aumento;
#O novo salário, após o aumento.
salário = float(input('Informe o salário: '))
if salário <= 280:
    percentual = '20%'
    aumento = salário * 0.2
    nsalário = salário + aumento
elif salário < 700:
    percentual = '15%'
    aumento = salário * 0.15
    nsalário = salário + aumento
elif salário < 1500:
    percentual = '10%'
    aumento = salário * 0.1
    nsalário = salário + aumento
elif salário >= 1500:
    percentual = '5%'
    aumento = salário * 0.5
    nsalário = salário + aumento
print(f'O salário atual é {salário}.\nO percentual de aumento é {percentual}.\nO valor do aumento é {aumento}.\nO salário ajustado é {nsalário}.')

#Ex 12: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
#do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não
#é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
#pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%
quant_hora = float(input('Quantas horas trabalhadas no mês? '))
valor_hora = float(input('Qual o valor da hora trabalhada? '))
salário_bruto = quant_hora * valor_hora
FGTS = salário_bruto * 0.11
INSS = salário_bruto * 0.1
if salário_bruto < 900:
    IR = salário_bruto * 0
    porcentagem_IR = 0
elif salário_bruto <= 1500:
    IR = salário_bruto * 0.05
    porcentagem_IR = 5
elif salário_bruto <= 2500:
    IR = salário_bruto * 0.1
    porcentagem_IR = 10
elif salário_bruto > 2500:
    IR = salário_bruto * 0.2
    porcentagem_IR = 20
total_descontos = salário_bruto - FGTS - INSS - IR
salário_líquido = salário_bruto - total_descontos
print(f'Salário bruto:({valor_hora:.0f}*{quant_hora:.0f}):R$ {salário_bruto:.0f},00')
print(f'(-) IR ({porcentagem_IR}%):{IR:.0f},00')
print(f'(-) INSS (10%):{INSS:.0f},00')
print(f'FGTS (11%):{FGTS:.0f},00')
print(f'Total de descontos:{total_descontos:.0f},00')
print(f'Salário líquido:{salário_líquido:.0f},00')

#Ex 13: Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
# outro valor deve aparecer valor inválido.
try:
    n = int(input('Digite um número: '))
    lista = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    print(f'O dia correspondente é {lista[n-1]}')
except:
    print('Número inválido')

#Ex 14: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
# a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
#ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média <= 4:
    conceito = 'E'
elif média <= 6:
    conceito = 'D'
elif média <= 7.5:
    conceito = 'C'
elif média <= 9:
    conceito = 'B'
elif média > 9:
    conceito = 'A'
if conceito in 'ABC':
    mensagem = 'Aprovado'
elif conceito in 'DE':
    mensagem = 'Reprovado'
print(f'As notas {nota1} e {nota2} têm média {média} e pussuem o conceito {conceito}.')
print(f'Você está {mensagem}!')

#Ex 15: Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
n1 = int(input('Informe o 1º lado: '))
n2 = int(input('Informe o 2º lado: '))
n3 = int(input('Informe o 3º lado: '))
if n1 < (n2 + n3) or n2 < (n1 + n3) or n3 < (n1 + n2):
    print('É um triângulo!')
    if n1 == n2 == n3:
        print('É um triângulo equilátero!')
    elif n1 != n2 != n3:
        print('É um triângulo escaleno!')
    if n1 == n2 or n2 == n3 or n3 == n1:
        print('É um triângulo isóceles!')
else:
    print('Não é um triângulo!')

#Ex 17: Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
import calendar
ano = int(input('Informe o ano: '))
if (calendar.isleap(ano)):
    print('É bissexto')
else:
    print('Não é bissexto')

#Ex 18:Faça um programa que peça uma data separando entre dia mês e escreva na tela se a data é válida.
dia = int(input('Informe o dia: '))
mês = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
if dia < 1 or dia > 31:
    print('data inválida')
elif mês < 1 or mês > 12:
    print('data inválida')
elif ano < 0:
    print('data inválida')
else:
    print('data válida')

#Ex 19: Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando
#os termos no plural a colocação do "e", da vírgula entre outros.
num = int(input('Digite um número: '))
números = str(num)
lista = list(números)
if len(lista) == 3:
    if '1' in lista[0]:
        casa_cent = 'centena'
    else:
        casa_cent = 'centenas'
    if '1' in lista[1]:
        casa_dec = 'dezena'
    else:
        casa_dec = 'dezenas'
    if '1' in lista[2]:
        casa_uni = 'unidade'
    else:
        casa_uni = 'unidades'
    print(f'{lista[0]} {casa_cent}, {lista[1]} {casa_dec} e {lista[2]} {casa_uni}.')

elif len(lista) == 2:
    casa_cent = 'centena'
    if '1' in lista[0]:
        casa_dec = 'dezena'
    else:
        casa_dec = 'dezenas'
    if '1' in lista[1]:
        casa_uni = 'unidade'
    else:
        casa_uni = 'unidades'
    print(f'0 centena, {lista[0]} {casa_dec} e {lista[1]} {casa_uni}.')

elif len(lista) == 1:
    casa_cent = 'centena'
    casa_dec = 'dezena'
    if '1' in lista[0]:
        casa_uni = 'unidade'
    else:
        casa_uni = 'unidades'
    print(f'0 centena, 0 dezena e {lista[0]} {casa_uni}.')

#Ex 21: Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
#de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
valorSaque = int(input('Valor do saque: R$ '))
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')

#Ex 22: Faça um programa que peça um número inteiro e determine se ele é par ou impar.
num = int(input('Informe um número: '))
if num % 2 == 0:
    print('É par!')
else:
    print('É ímpar!')

#Ex 23: Faça um programa que peça um número e informe se o número é inteiro ou decimal.
num = float(input('Informe um número: '))
f = (type(num))
if int:
    print('É inteiro!')
if float:
    print('Não é inteiro!')

#Ex 25: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. O programa deve no final emitir uma classificação
#sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
lista = []
lista.append(input('Telefonou para a vítima? [S/N]').upper())
lista.append(input('Esteve no local do crime? [S/N]').upper())
lista.append(input('Mora perto da vítima? [S/N]').upper())
lista.append(input('Devia para a vítima? [S/N]').upper())
lista.append(input('Já trabalhou com a vítima? [S/N]').upper())
num = lista.count('S')
if num == 5:
    print('Assassino')
elif num == 2:
    print('Suspeito')
elif num > 2:
    print('Cúmplice')
else:
    print('Inocente')
print(lista)

#Ex 26: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool: Até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
#Gasolina: Até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
#calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
tipo = input('Qual o tipo de combustível? [G/A]').upper()
litro = int(input('Quantos litros quer colocar? '))
if tipo == 'A':
    if litro < 21:
        preço_litro = 1.9 - (1.9 * 0.03)
        valor = litro * preço_litro
        print(f'O preço a ser pago será {valor}.')
    if litro >= 21:
        preço_litro = 1.9 - (1.9 * 0.05)
        valor = litro * preço_litro
        print(f'O preço a ser pago será {valor}.')
if tipo == 'G':
    if litro < 21:
        preço_litro = 2.5 - (2.5 * 0.04)
        valor = litro * preço_litro
        print(f'O valor a ser pago será {valor}.')
    if litro >= 21:
        preço_litro = 2.5 - (2.5 * 0.06)
        valor = litro * preço_litro
        print(f'O valor a ser pago será {valor}.')

#Ex 28: O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites
#para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
#o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
opção_carne = input('Peça de carne:\n[1]Filé duplo:\n[2]Alcatra:\n[3]Picanha\nSua opção: ')
quantidade = int(input('Quantidade de kilos: '))
pagamento = input('Pagamento com cartão Tabajara: [S/N]').upper()
if opção_carne == '1':
      peça_carne = 'Filé duplo'
      if quantidade > 5:
            preço_carne = 5.8
      else:
            preço_carne = 4.9

if opção_carne == '2':
      peça_carne = 'Alcatra'
      if quantidade > 5:
            preço_carne = 6.8
      else:
            preço_carne = 5.9

if opção_carne == '3':
      peça_carne = 'Picanha'
      if quantidade > 5:
            preço_carne = 7.8
      else:
            preço_carne = 6.9

if pagamento == 'N':
      preço_final = quantidade * preço_carne
else:
      preço_final = (quantidade * preço_carne)
      preço_final = preço_final - (preço_final * 0.05)

print(f'Opção carne: {opção_carne}.')
print(f'Quantidade: {quantidade} kg.')
print(f'Desconto: {pagamento}.')
print(f'Preço final: R${preço_final:.2f},00.')
