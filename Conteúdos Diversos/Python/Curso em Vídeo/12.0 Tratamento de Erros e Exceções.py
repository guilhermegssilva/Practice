try: #O programa tentará excutar a ação identada, é uma cláusula obrigatória
    a= int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: #Caso aconteça algum erro, será executado a ação identada, é uma cláusula obrigatória
    print('Tivemos um problema')


try: #O programa tentará excutar a ação identada, é uma cláusula obrigatória
    a= int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: #Transforma o erro em uma varíavel, podendo esta ser colocada em um print formatado
    print(f'O problema encontrado foi <{erro}> .')

else: #Caso o programa não apresente problemas será executado a ação identada, é uma cláusula opcional
    print(f'O resultado é {r:.1f}')

finally: #Será executada independente de apresentar ou não um erro, é uma cláusula opcional
    print('Volte sempre! Muito obrigado!')



try: #O programa tentará excutar a ação identada, é uma cláusula obrigatória
    a= int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Caso o programa apresente esse erro em específico (caso haja mais de um deverá ser posto entre parênteses)(Erro com o tipo digitado)
    print('Tivemos problemas com os tipos de dados que você digitou')
except ZeroDivisionError: #Caso o programa apresente esse erro em específico (tentativa de divisão por zero)
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt: #Caso o programa apresente esse erro em específico (O programa foi interrompido pelo usuário)
    print('O usuário não informou nenhum dado')
else: #Caso o programa não apresente problemas será executado a ação identada, é uma cláusula opcional
    print(f'O resultado foi {r:.1f}')
finally: #Será executada independente de apresentar ou não um erro, é uma cláusula opcional
    print('Volte sempre! Muito obrigado!')