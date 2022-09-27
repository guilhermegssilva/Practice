#Classes e Objetos
class Dog:
    def __init__(self, name, age): #Características da classe criada
        self.name = name
        self.age = age

    def get_name(self): #Função que retorna o nome do cachorro
        return self.name

    def get_age(self): #Função que retorna a idade do cachorro
        return self.age

    def set_age(self, age): #Função que altera a idade de um objeto
        self.age = age

d1 = Dog('Tim', 34)
d1.set_age(23) #A idade do objeto d1 será mudada
print(f'O cachorro se chama {d1.get_name()} e tem {d1.get_age()} anos.') #Entre colchetes a função da classe está sendo utilizada com cada um dos objetos
d2 = Dog('Bill', 12)
print(f'O cachorro se chama {d2.get_name()} e tem {d2.get_age()} anos')

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self): #Função que retorna a nota dos objetos da classe Student
        return self.grade

class Course:  # Função que vai adicionar estudantes em um determinado curso
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  #O objeto é uma lista vazia (Que não faz parte das características da classe)

    def add_student(self, student):  #Função que adiciona um estudante na lista students
        if len(self.students) < self.max_students:  #Se o tamanho da lista students for menor do que max_students
            self.students.append(student)  #append o estudante no objeto students (Que é uma lista)


    def get_average_grade(self):
        value = 0
        for student in self.students: #Para cada objeto student na lista students
            value = value + student.get_grade() #Variável recebe ela mesma somada à nota do student
        return value / len(self.students) #Retorna o valor dividido pelo tamanho da lista students

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)
course = Course('Science', 2)  #A classe course com o nome do curso e o número máximo de estudantes
course.add_student(s1)  #Serão adicionados 2 estudantes no curso
course.add_student(s2)
print(course.students[0].name)  #Escreve na tela o estudante na posição 0 da lista students
print(course.get_average_grade()) #Escreve na tela a média das notas dos alunos

#Herança
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old')

    def speak(self): #Caso a função tenha o mesmo nome da classe secundária, será usada a função da classe secundária
        print('I dont know that to say')
class Cat(Pet):
    def __init__(self, name, age, color): #Características que a classe Cat terá
        super().__init__(name, age) #Comando para adicionar as características da classe Pet
        self.color = color #Será adicionada as características que faltam

    def speak(self): #Caso a função dessa classe tenha o mesmo nome da classe principal, será usada essa função
        print('Meow')

    def show(self): #Dentro dessa classe a função show terá um parâmetro a mais (color)
        print(f'I am {self.name} and i am {self.age} and my color is {self.color}')
class Dog(Pet):
    def speak(self): #Caso a função dessa classe tenha o mesmo nome da classe principal, será usada essa função
        print('Bark')
p = Pet('Tim', 19)
p.speak()
p.show()
c = Cat('Bill', 34, 'brown')
c.speak()
c.show()
d = Dog('Jill', 25)
d.speak()
d.show()

#Métodos Estáticos
#É possível colocar as classes em um arquivo separado e depois importá-las para o seu arquivo principal usando o comando from e import
class Math:
    @staticmethod #São funções que não alteram a classe em si
    def add_5(num):
        return num + 5

    @staticmethod
    def add_10(num):
        return num + 10

    @staticmethod
    def run():
        print('run')

print(Math.add_10(2))
Math.run()
