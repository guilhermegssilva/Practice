#Special Methods
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

#str e repr servem para modificar uma string que será lida pelo usuário com o objetivo de se ter um entendimento melhor

    def __repr__(self): #Recomendado ter uma dessas em toda classe criada para se ter uma melhor legibilidade
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self): #O objetivo é ser o mais legível possível para o usuário, opcional de se ter
        return f'{self.fullname} - {self.email}'

    def __add__(self, other): #Função que pode somar valores que existam dentro de uma classe
        return self.pay + other.pay

    def __len__(self): #Função que pode medir a quantidade de caracteres de uma string dentro de uma classe
        return len(self.fullname()) #Retorna o número de caracteres do nome completo do objeto

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(repr(emp_1)) #Uma forma de se escrever as informações do método
print(emp_1.__repr__()) #Outra forma de se escrever as informações do método
print(emp_1 + emp_2) #Soma os salários de dois objetos
print(len(emp_1)) #Escreve o número de caracteres de determinado objeto

#Property Decorators
class Employee:
    def __init__(self, first, last): #Não é mais necessário criar um objeto email
        self.first = first
        self.last = last

    @property  # Com esse comando caso uma variável seja mudada fora da classe, a função realiza a ação com a variável atualizada
    def email(self):
        return f'{self.first}{self.last}@email.com'  # Retorna o objeto email mesmo que uma das variáveis tenha sido modificada

    @property #Caso fosse trocada a variável first e last, essa função retornaria o fullname atualizado
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter  # Caso o nome seja recebido sem espaços é possível separálo e atualizar as funções de acordo
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim' #A variável do objeto first é trocada
emp_1.fullname = 'Adam Hoffman' #Aqui o nome é recebido sem separação, então o setter.fullname separa a string em first e last e atualiza a função fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
