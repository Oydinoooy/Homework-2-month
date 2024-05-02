class MagicCalcultor:
    def __init__(self, numbers_1, numbers_2):
        self.numbers_1 = numbers_1
        self.numbers_2 = numbers_2

    def __add__(self, other):
        result = self.numbers_1 + other.numbers_1
        return f"Результат сложения: {result}"


    def __sub__(self, other):
        result = self.numbers_1 - other.numbers_1
        return f"Результат вычитание: {result}"

    def __mul__(self, other):
        result = self.numbers_1 * other.numbers_1
        return f"Результат умножения: {result}"


    def __truediv__(self, other):
        result = self.numbers_1 / other.numbers_1
        return f"Результат деления: {result}"


num1 = MagicCalcultor(15, 5)
num2 = MagicCalcultor(30, 15)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Названия книги: {self.name}, \nАвтор книги: {self.author}, \nГод выпуска - {self.year}"

    def book(self):
        print(f"Названия книги: {self.name}, \nАвтор книги: {self.author}, \nгод выпуска книги: {self.year}")

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year 

    def __ne__(self, other):
        return self.year != other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __le__(self, other):
        return self.year <= other.year


book1 = Book("Поющие в терновнике", "Колин Маккалоу", 1983)
book2 = Book("Три товарища", "Э. М. Ремарк", 1938)
book3 = Book("Гордость и предубеждение", "Джейн Остин", 1797)

book1.book()

book2.book()

book3.book()

print(book1 > book2 > book3)
print(book1 < book2 < book3)
print(book1 == book2 == book3)
print(book1 != book2 != book3)
print(book1 >= book2 >= book3)
print(book1 <= book2 <= book3)