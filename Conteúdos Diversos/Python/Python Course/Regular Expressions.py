#Regular Expressions
import re     #Comando para importar o módulo de Regular Expressions
r'string here \n' #Ao colocar um r no começo da string, ela evita qualquer escape characters como \n

text_to_search = '''
abcdefghijklmnopqurtuvwxyz                                             
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )                         

coreyms.com                                                 
321-555-4321
123.555.1234                                        
123*555*1234

Mr. Schafer
Mr Smith
Mrs. Robinson
Ms Davis
Mr. T

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern0 = re.compile(r'abc') #Cria uma variável para definir a expressão a ser encontrada

with open('data.txt', 'r') as f: #Comando para abrir um arquivo
    contents = f.read() #A variável contents recebe os conteúdos do arquivo
    matches = pattern0.finditer(contents) #Cria uma variável que conterá todas as combinações encontradas
    for match in matches: #Para cada combinação na lista de combinações encontradas dentro do arquivo
        print(match)


pattern1 = re.compile(r'coreyms\.com') #Caso a expressão possua um caractere especial eles devem ser antecedidos por \
pattern2 = re.compile(r'coreyms\.\.com') #Caso seja necessário encontrar mais de um caractere especial, cada um deles deve ser antecedido por \
pattern3 = re.compile((r'coreyms[.-]com')) #É possível colocar os caracteres entre parênteses, inclusive mais de um, retorna todas as vezes que ao menos um deles apareça
pattern4 = re.compile(r'\d\d\d') #Todas as combinações que possuam 3 dígitos
pattern5 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #Todas as combinações que possuam 3 dígitos seguidos de algum caractere e 4 dígitos no final')
pattern6 = re.compile(r'[89]4\d') #Todas as combinações que possuam 3 dígitos e o primeiro deles seja 8 ou 9 e o segundo seja 4
pattern7 = re.compile(r'[a-zA-Z]') #Todas as combinações que possuam letras de a até z, maiúsculas e minúsculas
pattern8 = re.compile(r'[1-7]') #Todas as combinações que possuam dígitos de 1 a 7
pattern9 = re.compile(r'[^a-zA-z]') #Todas as combinações que não sejam letras maiusculas e minúsculas (O sinal ^ nega o que vier após ele)
pattern10 = re.compile(r'\d{3}.\d{3}.\d{3}') #O número entre chaves indica o número de vezes que o comando \d irá aparecer
pattern11 = re.compile(r'Mr\.?') #O ? indica que o sinal antes dele '.', pode ou não aparecer no máximo 1 vez, serão mostrada ambas as combinações
pattern12 = re.compile(r'Mr\.?\s[A-Z]\w*') #O * indica que o sinal antes dele '\w', pode ou não aparecer, serão mostradas ambas as combinações
pattern13 = re.compile(r'(Mr|Ms|Mrs)') #Um grupo é formado entre parênteses, serão mostradas todas as combinações que se encaixam em algum dos parâmetros
pattern14 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') #Código para mostrar todos os nomes do texto
pattern15 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') #Código para mostrar todos os email do texto


urls = ''''https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') #Código para mostrar todas as urls do texto. São formados 3 grupos, cada um dentro de parênteses

matches = pattern.finditer(urls) #Cria uma variável que conterá todas as combinações encontradas
for match in matches: #Para cada combinação dentro das combinações encontradas
    print(match.group(0)) #Mostra todos os grupos juntos, no caso a expressão inteira encontrada
    print(match.group(3)) #Caso haja mais de um grupo cada número mostra um grupo distinto, começando da esquerda para a direita

modified_ulrs = pattern.sub(r'\2\3', urls) #O método .sub substitue as expressões encontradas por outras. Nesse caso as urls serão substituídas pelo 2º e 3º grupo de cada uma delas
print(modified_ulrs)

#Flags
#As flags colocadas após a expressão a ser encontrada a modificam permitindo outros resultados.
sentence = 'Start a sentence\nthen bring it to an end'
Pattern = re.compile(r'sTaRt', re.I) #Flag que indica para ignorar caracteres maiúsculos e minúsculos, permitindo ambos
Pattern1 = re.compile(r'ence.then', re.S) #O símbolo '.' indica que qualquer caractere não seja newline pode aparecer, a flag permite que possa ser um newline
Pattern2 = re.compile(r'eNce.ThEn', re.S|re.I) #O símbolo '|' permite que mais de uma flag seja adicionada na expressão.
Pattern3 = re.compile(r'^s\w+t$', re.I|re.M) #Flag que indica que os sinais '^' e '$' vão considerar o começo e  o final de múltiplas linhas de uma string
Matches = Pattern3.finditer(sentence)
for Match in Matches:
    print(Match)


#Comandos para encontrar strings
                                            #Será adicionado o comando seguido da expressão a ser encontrada
#.    - Any Character Except New Line
#\d   - Digit (0-9)
#\D   - Not a Digit (0-9)
#\w   - Word Character (a-z, A-Z, 0-9, _)
#\W   - Not a Word Character
#\s   - Whitespace (space, tab, newline)
#\S   - Not Whitespace (space, tab, newline)

#\b   - Word Boundary
#\B   - Not a Word Boundary
#^    - Beginning of a String
#$    - End of a String

#[]   - Matches Characters in brackets
#[^ ] - Matches Characters NOT in brackets
#|    - Either Or
#( )  - Group

#Quantifiers:
#*     - 0 or More
#+     - 1 or More
#?     - 0 or One
#{3}   - Exact Number
#{3,4} - Range of Numbers (Minimum, Maximum)

