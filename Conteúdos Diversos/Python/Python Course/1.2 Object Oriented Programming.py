#Classes e Métodos
class Employee:
    raise_amount = 1.04 #O valor pode ser definido aqui ao invés de ser na classe em si
    number_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.number_of_employees = Employee.number_of_employees + 1 #Cada vez que um objeto for criado a variável aumentará em 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #Quando o valor for chamado deve ser colocado o self. na frente

    @classmethod
    def set_raise_amt(cls, amount): #Usa a classe(cls) como argumento e muda o valor de raise_amount para todos os objetos da classe
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')  # As variáveis first, last, pay, recebem a string com a função split
        return cls(first, last, pay) #Retorna para uma variável os parâmetros do método

class Developer(Employee):
    raise_amount = 1.10 #O valor da variável será mudado apenas para os objetos pertencentes a essa classe

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None: #Se o valor de employees for None será criada uma lista vazia
            self.employees = []
        else:
            self.employees = employees #Ou então a lista recebe os employee que forem adicionados

    def add_emp(self, emp):
        if emp not in self.employees: #Se o objeto employee não estiver na lista ele será adicionado
            self.employees.append(emp)

    def remove_emp(self, emp): #Se o objeto employee estiver na lista ele será removido
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self): #Será escrito todos os employee que estão na lista
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
dev_1 = Developer('Tim', 'Jones', 70000)
dev_2 = Developer('Brian', 'Miller', 70000)
mgr_1 = Manager('Susan', 'Smith', 90000, [dev_1]) #O objeto mgr_1 gerencia o objeto dev_1

Employee.set_raise_amt(1.06) #Função que muda uma variável mesmo ela não estando definida inicialmente dentro da classe
emp_1.raise_amount = 1.05 #O valor de uma variável pode ser mudado para apenas um objeto específico

print(emp_1.pay) #Salário inicial
emp_1.apply_raise() #Função que aumenta o salário
print(emp_1.pay) #Salário após o aumento
print(emp_1.raise_amount) #Valor mudado da variável apenas para o objeto emp_1
print(emp_2.raise_amount) #a variável inicial é mudada por conta do @classmethod
print(Employee.number_of_employees) #Mostra o número de objetos employee criados
mgr_1.add_emp(dev_2) #É adicionado dev_2 na lista de employees
mgr_1.print_emps() #Escreve a lista de employee
mgr_1.remove_emp(dev_2) #É removido dev_2 da lista de employees



emp_str_1 = 'John-Doe-70000' #Informaçãoes são passadas em uma string separadas por hífen
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1) #Na classe Employee a função from_string é usada no objeto emp_str_1
print(new_emp_1.email)
print(new_emp_1.pay)




