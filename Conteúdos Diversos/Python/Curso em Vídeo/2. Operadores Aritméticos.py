#print('='*20)
#print(81**(1/2))
#print(125**(1/3))
#nome = input('Qual o seu nome')
#print(f'Prazer em te conhecer {nome:^20}!')
#print(f'Prazer em te conhecer {nome:20}!')
#print(f'Prazer em te conhecer {nome:=^20}!')
n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
s = n1+n2
d = n1/n2
m = n1*n2
sub = n1-n2
di = n1//n2
pot = n1**n2
#print(f'A soma é {s}, a divisão é {d:.3f}, a multiplicação é {m}, a subtração é {sub} a divisão inteira é {di} e a potência é {pot}')
print(f'A soma é {s}, a divisão é {d}, \n a multiplicação é {m}, \n a subtração é {sub}', end=' ')
print(f'a divisão inteira é {di} e a potência é {pot}')