from random import randint
from time import sleep
print('OLÁ, BEM VINDO AO JOGO DA ADIVINHAÇÃO.')
sleep(1)
print('EU PENSAREI EM UM NÚMERO E O SEU OBJETIVO É TENTAR ADIVINHAR EM QUAL DELES EU ESTOU PENSANDO NO MENOR NÚMERO DE TENTATIVAS POSSÍVEL.')
sleep(2.5)
while True:
    print('VAMOS LÁ!!!')
    sleep(1)
    print('OK, O NÚMERO ESTÁ ENTRE 1 E 100')
    sleep(1)
    cont = 0
    numero = randint(1, 101)
    while True:
        try:
            palpite = int(input('Qual é o seu palpite? '))
            cont = cont + 1
            if palpite < 1 or palpite > 100:
                print('Lembre-se que o número está entre 1 e 100.')
                continue
            elif palpite > numero:
                print('Menos...')
            elif palpite < numero:
                print('Mais...')
            elif palpite == numero:
                break
        except ValueError:
            print('Lembre-se de que o sua resposta deve ser um número.')
            continue

    print(f'Você acertou, o número era {numero}\nForam necessárias {cont} tentativas.\nPARABÉNS!!!')

    resposta = input('Quer jogar novamente? [S/N]').upper()
    while resposta not in 'SN':
        resposta = input('Sua resposta deve ser S ou N. Quer jogar novamente? [S/N]')
    if resposta == 'N':
        break
    elif resposta == 'S':
        print('Ok, Obrigado pela preferência!')
        sleep(1)
        print('REINICIANDO JOGO ...')
        sleep(1.5)

print('Está bem, obrigado por jogar.\nVolte sempre!')