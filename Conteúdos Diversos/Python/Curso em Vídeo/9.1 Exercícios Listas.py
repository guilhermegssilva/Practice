#Ex 78: Faça um pograma que leia 5 valores e guarde-os em uma lista. No final mostre qual foi o maior e menor
#valor digitado e sua respectiva posição na lista.
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c} ')))
print(f'Você digitou os valores {valores}.')
print(f'O valor mais baixo é {min(valores)} e está na posição ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}. ', end='')
print()
print(f'O valor mais alto é {max(valores)} e está na posição ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}. ', end='')

#Ex 79: Crie um programa onde o usuário possa digitar vários valores e coloque-os em uma lista. Caso o número já esteja
#lá ele não será adicionado. No final serão mostrados todos os valores únicos digitados em ordem crescente.
lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print(f'O número {num} foi cadastrado.')
    else:
        print(f'O número {num} já foi cadastrado.')
    resposta = input('Quer continuar?(S/N)').upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input('Resposta inválida. Digite novamente. (S/N)').upper()
    if resposta == 'N':
        break
lista.sort()
print(lista)

#Ex 80: Crie um programa onde o usuário possa digitar cinco valores e cadastre-os em uma lista já na posição certa.
#No final mostra a lista ordenada na tela.
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n<= lista(pos)
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos = pos + 1
print(f'Os valores digitados em ordem foram {lista}')

#Ex 81: Crie um programa que leia vários números e os coloque numa lista. Depois disso mostre: Quantos números foram
#digitados, a lista de números ordenada de forma decrescente e se o número 5 está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um número:')))
    resposta = input('Quer continuar? [S/N]').upper()
    while resposta not in 'SN':
        resposta = input('Resposta inválida.Digite novamente. [S/N]').upper()
    if resposta == 'N':
        break
lista.sort(reverse=True)
print(f'A lista possui {len(lista)} números.')
print(f'A lista em ordem decrescente fica {lista}.')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista.')

#Ex 82: Crie um programa que vai ler vários números e coloca-los em uma lista. Depois disso crie duas listas extras e
#coloque numa os números pares e em outra os números ímpares digitados. Ao final mostre o conteúdo das três listas.
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número')))
    resposta = input('Quer continuar?[S/N]').upper()
    while resposta not in 'SN':
        resposta = input('Resposta inválida.Digite novamente.[S/N]').upper()
    if resposta == 'N':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista original é {lista}.\nA lista com números pares é {listapar}.\nA lista com números ímpares é {listaimpar}.')

#Ex 83: Crie um programa que leia uma expressão qualquer que use parênteses. Seu programa deverá analisar se os parênteses
#estão abertos e fechados na ordem correta.
expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')


