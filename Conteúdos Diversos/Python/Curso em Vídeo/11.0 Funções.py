def lin(): #Comando para se criar uma função
    print('-=' * 30) #Deve ser identado
lin()
print('Curso em vídeo')
lin()
print('Aprenda Python')
lin()
print('Gustavo Guanabara')
lin()


def titulo(msg): #Função cuja a mensagem entre parênteses muda
    print('-=' * 30)
    print(msg) #Irá escrever a mensagem que está entre parênteses

titulo('Curso em vídeo') #Cada vez que o código chegar nessa linha ele vai executar a função
titulo('Aprenda Python') #Cada vez que o código chegar nessa linha ele vai executar a função
titulo('Gustavo Guanabara') #Cada vez que o código chegar nessa linha ele vai executar a função


def soma(a, b): #Define uma função que soma dois elementos
    print(f'A = {a} e B = {b}')
    s = a + b #s recebe a soma dos elementos
    print(f'A + B recebe o valor de {s}') #Escreve s na tela
soma(4, 5) #Se não explicitado o primeiro elemento será a e o segundo será b
soma(b=8, a=9) #Os valores de a e b serão trocados de acordo
soma(2, 1)


def contador(* num): #Função para contar a quantidade de números. O asterisco desempacota os números
    print(num) #Escreve os números em uma tupla
    tam = len(num) #Variável tamanho vai ser igual ao tamanho da tupla
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    for valor in num: #Para cada valor dentro da tupla
        print(f'{valor} ',end=' ') #Escreve os valores dentro de cada tupla
        print()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lista): #Função para dobrar os números dentro de uma lista
    pos = 0
    while pos < len(lista): #Enquanto a posição for menor que o tamanho da lista
        lista[pos] = lista[pos] * 2 #Lista na posição 'x' recebe o valor dela mesma * 2
        pos = pos + 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def sum(* val): #Função para somar os números. O asterisco desempacota os números
    p = 0
    for numero in val: #Para cada número dentro da tupla
        p = p + numero #p recebe ele mesmo mais o número
    print(f'Somando os valores temos {p}.')

sum(1, 2, 3)
sum(8, 9, 5)


def sum(a=0, b=0, c=0): #Os parâmetros recebem o valor 0 como padrão
    s = a + b + c
    print(s)
sum(1, 2, 3)
sum(0, 2, 0)
sum(3) #Mesmo com parâmetros a menos a função ainda funciona


def área(larg, comp): #Função para calcular área
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a} metros quadrados.')

l = int(input('Largura:')) #Os inputs do usuário estarão fora da função
c = int(input('Comprimento'))#Os inputs do usuário estarão fora da função
área(l, c) #O nome deve ser o mesmo da função(área)


def sum(a=0, b=0, c=0): #Os parâmetros recebem o valor 0 como padrão
    s = a + b + c
    return(s) #return retorna o resultado da função para uma varíavel colocada na frente dela

r1 = sum(1, 2, 3)
r2 = sum(0, 2, 0)
r3 = sum(4)


def fatorial(num=0): #Função para calcular o fatorial de um número
    f = 1
    for c in range(num, 0, -1): #Para cada número de num até 0
        f = f * c
    return f #O f será retornado para as variáveis que antecedem a função

f1 = fatorial(5)
f2 = fatorial(10)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')