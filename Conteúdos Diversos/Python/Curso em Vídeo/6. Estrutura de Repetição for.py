for c in range(0,6): #Escreve Oi 6 vezes
    print('Oi')
print('FIM')

for c in range(0,6): #Escreve Oi e FIM 6 vezes alternadamente
    print('Oi')
    print('FIM')

for c in range(6,0,-1): #Conta de seis até 1
    print(c)

for c in range(0,7,2): #Conta de 0 até 7 pulando de dois em dois
    print(c)

n = int(input('Digite um número')) #Conta de 0 até o número digitado
for c in range(0,n+1):
    print(c)

i = int(input('Início')) #Conta do início até o final usando os passos dados
f = int(input('Fim'))
p = int(input('Passo'))
for c in range(i,f+1,p):
    print(c)
print('FIM')

for c in range(0,3): #Escreve a varíavel n 3 vezes
    n = int(input('Digite um número'))
print('FIM')

s = 0
for c in range(0,4): #Soma os 4 números lidos
    n = int(input('Digite um número'))
    s = s+n
print(f'O total da soma foi {s}')