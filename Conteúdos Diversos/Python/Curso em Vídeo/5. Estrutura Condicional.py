tempo = int(input('Quantos anos tem seu carro?'))
if tempo>= 3:
    print('Seu carro é velho')
else:
    print('Seu carro é novo')
print('--Fim--')

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro velho'if tempo>=3 else 'Carro novo')

nome = input('Qual o seu nome?')
if nome=='Guilherme':
    print('Que nome lindo')
else:
    print('Que nome normal')
print(f'Bom dia {nome}')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2) / 2
print(f'Sua média é {m:.1f}')
if m>=6:
    print('Parábens, você está acima da média!')
else:
    print('Que pena, você está abaixo da média')