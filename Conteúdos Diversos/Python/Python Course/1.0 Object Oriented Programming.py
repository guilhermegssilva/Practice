#Classes e Objetos
class SoftwareEngineer: #Define o nome da classe. A classe pode receber qualquer característica para moldá-la do jeito que quiser
    alias = 'Keyboard Magician' #Define uma característica da classe. Essa por sua vez, será compartilhada entre todos os objetos dentro dela
    def __init__(self, name, age, level, salary): #Entre parênteses será colocado todas as características do objeto que será criado
        self.name = name       #Essas são as características que cada objeto dentro dessa classe terá
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f'{self.name} is writing code ...') #Função que pode ser usada com um objeto

    def code_language(self, language):
        print(f'{self.name} is writing code in {language}.') #Essa função necessita de uma linguagem como parâmetro

    def information(self):
        information = f'name = {self.name}, age = {self.age}, level = {self.level}'
        return information

    def __eq__(self, other): #Função que compara se os valores entre os dois objetos são iguais
        return self.name == other.name and self.age == other.age

se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)  #Comando que cria o objeto, entre parênteses estão as varíaveis que ele irá receber
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000) #Todos os objetos dentro da classe terão as mesmas características
se3 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
print(f'O nome é {se1.name} e a idade é {se1.age}')  #Escreverá a variável name e idade do objeto se1
print(se1.alias) #Escreve o apelido do objeto se1
print(se1.code()) #Chama a função e a executa conforme o objeto especificado
print(se1.code_language('Python')) #Chama a função e executa ela com o parâmetro dado
print(se1.information()) #Chama a função que descreve as características do objeto designado
print(se2 == se3) #Retorna True se os valores entre os dois objetos forem iguais

#Herança
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working.') #Caso uma das classes secundárias tenha uma função com o mesmo nome, será usada aquela função ao invés desta

class Programmer(Employee): #Essa classe herdará todas as características da classe entre parênteses
    def __init__(self, name, age, salary, level): #Função que indica as características que a classe terá
        super().__init__(name, age, salary) #Função que usa as características da classe principal(Employee) como base, é usada para quande se quer adicionar alguma característica extra
        self.level = level #Será adicionada as características extras que não estão na classe principal(Employee)

    def debug(self):
        print(f'{self.name} is debugging.') #Função só funciona em conjunto com a clase Programmer

    def work(self):
        print(f'{self.name} is coding.')

class Designer(Employee): #Essa classe herdará todas as características da classe entre parênteses
    def draw(self):
        print(f'{self.name} is drawing.') #Função só funciona em conjunto com a classe Designer

    def work(self):
        print(f'{self.name} is designing.')

programmer1 = Programmer('Max', 25, 5000, 'Junior')
print(f'{programmer1.name} is working.')
print(programmer1.name, programmer1.age)
print(programmer1.level)
programmer1.debug()
programmer1.work()

designer1 = Designer('Brian', 23, 7000)
print(designer1.name)
designer1.work()
designer1.draw()








