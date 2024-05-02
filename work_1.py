"""Создайте класс Fruits c атрибутами - (name, color, weight)
Создайте три объекта класса и с помощью метода info выведите информацию о каждом фрукте """

class Fruits:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f"Name - {self.name}, Color - {self.color}, Weight - {self.weight}")

list_fruits = Fruits("Apple", "Red", "250 g")
list_fruits_2 = Fruits("Orange", "Orange", "190 g")
list_fruits_3 = Fruits("Banana", "Yellow", "160 g")
list_fruits_4 = Fruits("Lime", "Green",  "130 g")

list_fruits.info()
print(list_fruits.info)
list_fruits_2.info()
print(list_fruits_2.info)
list_fruits_3.info()
print(list_fruits_3.info)
list_fruits_4.info()
print(list_fruits_4.info)


"""Доп. задание:
Создайте класс Heroes с атрибутами name, role и health.
Реализуйте метод info(), который выводит информацию о персонаже, включая его имя, роль и количество здоровья."""

class Heroes:
    def __init__(self, name, role, health):
        self.name = name
        self.role = role
        self.health = health

    def info(self):
        print(f"Name - {self.name}, Role - {self.role}, Health - {self.health}")

sot_heroes = Heroes("Симба", "Главный герой", "100%")
sot_heroes_2 = Heroes("Муфаса", "Отец Симбы", "0%")
sot_heroes_3 = Heroes("Сараби", "Мать Симбы", "60%")
sot_heroes_4 = Heroes("Нала", "Подруга Симбы", "100%")
sot_heroes_5= Heroes("Рафики", "Мандрил-шаман", "50%")

sot_heroes.info()
print(sot_heroes.info)
sot_heroes_2.info()
print(sot_heroes_2.info)
sot_heroes_3.info()
print(sot_heroes_3.info)
sot_heroes_4.info()
print(sot_heroes_4.info)
sot_heroes_5.info()
print(sot_heroes_5.info)


"""Создайте несколько объектов класса Heroes с различными именами, расами и здоровьем.
Используйте метод info() для вывода информации о каждом созданном персонаже. 
Так же создайте действие для вашего героя."""

class Heroes:
    def __init__(self, name, race, health):
        self.name = name
        self.race = race
        self.health = health
        

    def info(self):
        print(f"Имя - {self.name}, Роль - {self.race}, Здоровье - {self.health}")

    def role1 (self):
            print(f"{self.name} Бежит со скоростью 30 км/ч")
         
    def role2(self):
            print(f"{self.name} Перепрыгиват препятствие!")
        
    def role3(self):
            print(f"{self.name} Наносит удар!")

heroes = Heroes("Макс", "Атлетик", "90%")
heroes_2 = Heroes("Аня", "Шестовик", "95%")
heroes_3 = Heroes("Дима", "Боксёр", "88%")
    
heroes.info()
print(heroes.name)
heroes_2.info()
print(heroes_2.name)
heroes_3.info()
print(heroes_3.name)
heroes.role1()
heroes.role2()
heroes.role3()