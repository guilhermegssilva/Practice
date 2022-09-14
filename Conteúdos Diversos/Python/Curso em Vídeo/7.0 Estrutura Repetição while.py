c = 1
while c < 10:
    print(c)
    c = c+1

n = 1
while n != 0:
    n = int(input('Digite um valor'))

r = 'S'
while r == 'S':
    n = int(input('Digite um número'))
    r = input('Quer continuar?[S/N]').upper()

n = 1
par = 0
imp = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n%2 == 0:
        par = par+1
    else:
        imp = imp+1
print(f'VocÊ digitou {par} números pares e {imp} números ímpares.')
print('Fim')

cont = 0
while True: #Repetirá o código até ser usada a função break
    print(cont, end=' ')
    cont = cont + 1

n = 0
s = 0
while True:
    n = int(input('Digite um número'))
    if n == 999:
        break #A estrutura while será parada a partir desse ponto
    s = n + s #A soma não irá considerar o número 999 pois ele é o flag que fez a quebra do laço
print(f'A soma vale {s}')


