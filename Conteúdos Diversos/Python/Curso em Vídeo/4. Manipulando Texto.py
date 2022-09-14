#FATIAMENTO
frase = 'Curso em Vídeo Python'
#[inicio:final:passos]
print(frase[9]) #Busca índice específico na string
print(frase[9:13]) #Escreve a string de um número até o outro no caso do nove ao 12, o último será ignorado
print(frase[9:21]) #Escreve a string de um número até o outro, caso o último não exista irá parar antes
print(frase[9:21:2]) #Inicia a string do primeiro índice até o último pulando de dois em dois
print(frase[:5]) #Inicia a string do caractere zero e vai até o 4, sendo que o 5 é ignorado
print(frase[15:]) #Inicia a string do 15º caractere até o último
print(frase[9::3]) #Inicia no caractere 9 indo até o final e pulando de três em três

#ANÁLISE
print(len(frase)) #Escreve na tela o número total de caracteres numa string incluindo espaços
print(frase.count('o')) #Conta quantas vezes a letra 'o' aparece na string
print(frase.count('o', 0, 13)) #Conta quantas vezes a letra 'o' aparece do caractere 0 até o 12, o 13 é ignorado
print(frase.find('deo')) #Indica onde foi encontrada essa sequencia de caracteres
print(frase.find('Android')) #Caso a palavra não seja encontrada na string será retornado o resultado -1
print('Curso' in frase) #Escreve na tela se existe ou não uma sequencia de caracteres na string(True or False)
print(frase.lower().find('vídeo')) #Transforma toda a astring em minúsculo depois indica a posição em que está a palavra especificada

#TRANSFORMAÇÃO
print(frase.replace('Python', 'Android')) #Substitui uma palavra por outra na string
print(frase.upper()) #A string será escrita toda em maiúsculo
print(frase.lower()) #A string será escrita toda em minúsculo
print(frase.capitalize()) #Deixa apenas o primeiro caractere de uma string em maiúsculo
print(frase.title()) #Deixa em letra maiúscula todas as letras iniciais de cada palavra
print(frase.upper().count('O')) #Transforma toda a string em maiúsculo depois contará quantas vezes aparece determinado caractere

frase = 'Aprenda Python'
print(frase.strip()) #Remove todos os espaços desnecessários no início e no final da string
print(frase.rstrip()) #Remove somentes os espaços no final da string
print(frase.lstrip()) #remove somente os espaços no começo da string

#DIVISÃO
frase = 'Curso em Vídeo Python'
print(frase.split()) #Quebra todas palavras de uma string, transformando-as em uma lista, cada palavra recebe uma nova indexação de caracteres começando do zero
dividido = frase.split()
print(dividido[2][3]) #Mostra na tela o terceiro caractere do segundo elemento da lista começando do zero

#JUNÇÃO
print('-'.join(frase)) #Junta os elementos de uma string, entre aspas será definido como será feita a separação




