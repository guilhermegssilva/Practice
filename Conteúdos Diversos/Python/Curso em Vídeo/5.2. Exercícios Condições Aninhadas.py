#Ex 36: Escreva um programa que vai perguntar o salário, o valor da casa e em quantos anos irá pagar
#Calcule o valor da prestação sendo que ela não pode exceder 30% ou ele será negado.

val = float(input('Qual o valor total da casa?'))
sal = float(input('Qual o valor total do seu salário'))
t = float(input('Em quantos anos deseja pagar?'))*12
mens = val/t
if mens>(sal*0.3):
    print('O empréstimo foi negado')
else:
    print('Empréstimo feito com sucesso')

#Ex 38: Escreva um programa que leia dois números e diga qual deles é o maior ou se os dois são iguais.

num1 = float(input('digite um valor'))
num2 = float(input('Digite outro valor'))
if num1 > num2:
    print(f'{num1} é o maior valor')
elif num2 > num1:
    print(f'{num2} é o maior valor')
elif num1 == num2:
    print(f'{num1} e {num2} são o mesmo valor')

#Ex 39: Faça um programa que leia a data de nascimento de uma pessoa e diga se ela deve se alistar, caso sim,
#quanto tempo falta ou se já passou da hora.

from datetime import datetime
data = int(input('Qual o seu ano de nascimento'))
ano = datetime.now().year
prazo = (data+18)
if (ano-data)<18:
    print(f'Você ainda deve se alistar, faltam {prazo-ano} anos')
elif (ano-data)==18:
    print('Você deve se alistar esse ano')
else:
    print(f'Já passou {abs(ano-prazo)} anos da hora de se alistar')

#Ex 40: Crie um programa que leia duas notas de um aluno e diga sua média e diga se ele foi ou não aprovado.

n1 = float(input('Informe a primeira nota'))
n2 = float (input('Informe a segunda nota'))
média = (n1+n2)/2
print(f'Sua média é {média}')
if média<5:
    print('Reprovado')
elif média>=5 and média<7:
    print('Recuperação')
elif média>=7:
    print('Aprovado')

#Ex 42: Desenvolva um programa que leia três comprimentos de retas e diga se elas podem ou não formar um triângulo
#caso formem, diga que tipo de triângulo será formado.

a = float(input('Qual o tamnanho da primeira reta?'))
b = float(input('Qual o tamanho da segunda reta?'))
c = float(input('Qual o tamanho da terceira reta?'))
if a<b+c and b<c+a and c<b+a:
    print('É um triângulo', end=(' '))
    if a == b and b == c:
        print('Equilátero')
    elif a!=b and b!=c and c!=a:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não é um triângulo')

#Ex 43: Desenvolva uma lógia que leia a altura e o peso de uma pessoa e calcule o seu IMC e mostre na tela o resultado.

peso = float(input('Qual o seu peso?'))
alt = float(input('Qual a sua altura'))
imc = peso/(alt*alt)
if imc>=40:
    print('Obesidade mórbida')
elif imc>=30:
    print('Obesidade')
elif imc>=25:
    print('Sobrepeso')
elif imc>=18.5:
    print('Peso ideal')
else:
    print('Abaixo do peso')

#Ex 44: Faça um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento.
print(f'{"Lojas Guanabara":=^40}')
preço = float(input('Qual o preço do produto?'))
print('''Escolha a opção de pagamento:
[1]Á vista em dinheiro
[2]Á vista no cartão
[3]2x no cartão
[4]3x no cartão''')
opção = int(input('Qual a opção de pagamento?'))
if opção==1:
    valor = preço-(preço*0.1)
    print(f'O valor a ser pago será {valor} reais')
elif opção==2:
    valor = preço-(preço*0.05)
    print(f'O valor a ser pago será {valor} reais')
elif opção==3:
    print(f'O valor a ser pago será {preço} reais\nem 2 parcelas cada parcela sera {preço/2} reais')
elif opção==4:
    valor = preço+(preço*0.2)
    print(f'O valor ser pago será {valor} reais')
else:
    print('Essa opção é inválida')

#Ex 45: Faça um programa que jogue jokenpô com o jogador.

from random import randint
print('''Suas opções:
[1]Pedra
[2]Papel
[3]Tesoura''')
pl = int(input('Qual a sua jogada?'))
pc = randint(1,3)
if pl == pc:
    print('Empate!')
elif pl==1 and pc==2:
    print('O computador venceu!')
elif pl==2 and pc==3:
    print('O computador venceu')
elif pl==3 and pc==1:
    print('O computador venceu!')
elif pl==1 and pc==3:
    print('Player venceu!')
elif pl==2 and pc==1:
    print('Player venceu!')
elif pl==3 and pc==2:
    print('Player venceu!')
else:
    print('Jogada inválida')










