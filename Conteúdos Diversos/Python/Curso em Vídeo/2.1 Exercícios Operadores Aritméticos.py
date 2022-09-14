#Ex 05 e 06: Crie um programa que leia um número e mostre seu sucessor, seu antecessor, seu dobro,
#seu triplo e sua raiz quadrada.
num = int(input('Digite um número'))
print(f'O número antecessor é {num-1} e o sucessor é {num+1}')
print(f'O dobro desse número é {num*2}, o triplo desse número é {num*3} e a raiz quadrada é {num**(0.5):.2f}')

#Ex 07: Crie um programa que leia duas notas de um aluno e calcule sua média.
nota1 = int(input('Insira a primeira nota'))
nota2 = int(input('Insira a segunda nota'))
nf = (nota1 + nota2)/2
print(nf)

#Ex 08: Desenvolva um programa que leia um valor em metros e converta-o para cm e mm.
valorm = int(input('Qual o valor em metros ?'))
valorcm = valorm*100
valormm = valorm*1000
print(f'O valor em cm é {valorcm} e o valor em mm é igual a {valormm}')

#Ex 09: Faça um programa que leia na tela um número e mostre na tela a sua tabuada.
num = int(input('Digite um número'))
print(f'{num}*1 é igual a {num*1}')
print(f'{num}*2 é igual a {num*2}')
print(f'{num}*3 é igual a {num*3}')
print(f'{num}*4 é igual a {num*4}')
print(f'{num}*5 é igual a {num*5}')
print(f'{num}*6 é igual a {num*6}')
print(f'{num}*7 é igual a {num*7}')
print(f'{num}*8 é igual a {num*8}')
print(f'{num}*9 é igual a {num*9}')
print(f'{num}*10 é igual a {num*10}')

n = int(input("digite o número desejado:"))
x = str("   ")
print(f'{n}X1 = {n*1}', end="")
print(f'{x*5:<}', end="")
print(f'{n}X6 = {n*6}')
print(f'{n}X2 = {n*2}', end="")
print(f'{x*5:<}', end="")
print(f'{n}X7 = {n*7}')
print(f'{n}X3 = {n*3}', end="")
print(f'{x*5:<}', end="")
print(f'{n}X8 = {n*8}')
print(f'{n}X4 = {n*4}', end="")
print(f'{x*5:<}', end="")
print(f'{n}X9 = {n*9}')
print(f'{n}X5 = {n*5}', end="")
print(f'{x*5:<}', end="")
print(f'{n}X10 = {n*10}')

#Ex 10: Crie um programa que mostre quantos dinheiro uma pessoa tem na carteira e quantos
#dólares ela pode comprar.
din = int(input('Quanto dinheiro você tem?'))
dol = din/3.27
print(f'Você tem {dol:.2f} dólares na sua carteira')

#Ex 11: Faça um programa que leia a altura e a largura de uma parede e calcule quanta tinta será necessária
#para pintála sabendo que cada litro de tinta pinta uma área de 2m quadrados.
alt = int(input('Qual a altura da parede?'))
lar = int(input('Qual a largura da parede?'))
area = alt*lar
print(f'A sua parede vai precisar de {area/2} baldes de tinta')

#Ex 12: Faça um algoritmo que leia o preço de um produto e mostre seu valor com 5% de desconto.
prod = int(input('Informe o preço do produto'))
liq = prod-(prod*0.05)
print(f'O preço com desconto fica por {liq}')

#Ex 13: Faça um programa que leia o salário de um funcionário e mostre ele com 15% de aumento.
sal = int(input('Informe salário atual'))
nsal = sal+(sal*0.15)
print(f'Seu novo salário será {nsal}')

#Ex 14: Escreva um programa que converta uma temperatura em ºC para ºF.
tem = float(input('Qual a temperatura?(ºC)'))
temf = (tem*1.8) + 32
print(f'A temperatura em ºF é {temf}')

#Ex 15: Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e calcule o valor a
#ser pago sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
num1 = float(input('Quantos dias alugados?'))
num2 = float(input('Quantos km percorridos?'))
valor = (num1*60) + (num2*0.15)
print(f'O valor a ser pago será R${valor}')