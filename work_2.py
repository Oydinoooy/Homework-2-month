# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself(представиться), который бы распечатывал всю информацию о человеке
# 3. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом объекта experience


# Доп. задание
# 1. Добавить в класс Teacher атрибут класса salary = 0
# 2. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждый год опыта.
# 3. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age 
        self.is_married = is_married


    def introduce_myself (self):
        print(f"Полное имя - {self.fullname}, Возраст - {self.age}, Семейное положение - {self.is_married}")


num1 = Person("Владимир", "30 лет", "Женат")
num2 = Person("Анастасия", "20 лет", "Не замужем")
num3 = Person("Александр", "27 лет", "Женат")
num4 = Person("Михаил", "21 лет", "не женат")
num5 = Person("Евгения", "28 лет", "Замужем")

num1.introduce_myself()
num2.introduce_myself()
num3.introduce_myself()
num4.introduce_myself()
num5.introduce_myself()

class Teacher(Person):

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 0
    
    def сounting_the_salary(self):
        for i in range(self.experience):
            self.salary+= 3000
        print(f"Зарплата - {self.salary}")

    
    def introduce_myself(self):
        print(f"Полное имя - {self.fullname}, Возраст - {self.age}, Семейное положение - {self.is_married}, Опыт - {self.experience}")

teach = Teacher("Анна", "25 лет", "Замужем", 2)
teach2 = Teacher("Володя", "33 года", "Женат", 10)
teach3 = Teacher("Алина", "52 года", "Замужем", 20)


teach.introduce_myself()
teach.сounting_the_salary()
teach2.introduce_myself()
teach2.сounting_the_salary()
teach3.introduce_myself()
teach3.сounting_the_salary()


