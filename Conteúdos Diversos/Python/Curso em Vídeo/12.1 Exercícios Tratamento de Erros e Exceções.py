#Ex 113: Crie um programa que tente ler um número digitado pelo usuário e apresente uma mensagem de erro caso o número digitado
#não esteja dentro dos parâmetros.
while True:
    try:
        num = int(input('Digite um número inteiro: '))
        print(f'O número digitado foi {num}.')
        break
    except Exception as erro:
        print(f'Ocorre um erro <{erro}>.')

#Ex 114: Crie um código em Python que teste se o site Pudim está acessível no computador usado.
import urllib, urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
    print('Consegui acessar o site do pudim com sucesso')
except:
    urllib.error.URLError
    print('O site não está acessível no momento')


