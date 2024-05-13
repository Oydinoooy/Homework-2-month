import sqlite3

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS customs (
               id INTEGER PRIMARY KEY,
               name VARCHAR (100) NOT NULL,
               surname VARCHAR (100) NOT NULL,
               age INTEDER NOT NULL ,
               email TEXT NOT NULL,
               balance DOUBLE (10, 2) DEFAULT 0.0,
               props VARGHAR (100) NOT NULL,
               is_active BOOLEAN DEFAUL FALSE

);""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None 
        self.age = 0
        self.email = None
        self.balanсe = 0
        self.props = None
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name 
        self.surname = surname
        self.age = age
        self.email = email
        cursor.execute(f"""INSERT INTO customs (name, surname, age, email, balanсe, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}', 0, 0, True);""")
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f"""UPDATE customs SET balanse = balanсe + {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balanсe += amount 

    def minus(self, amount):
        cursor.execute(f"""UPDATE customs SET balanse = balance - {amount} WEHER email = '{self.email}'""")
        connect.commit()
        if amount > self.balanсe:
            print("Извините, но на счету не осталось денег!")
        
        else:
            self.balanсe -= amount
            print(f"Вы сняли {amount} \nВаш баланс {self.balanсe}")

    def __str__(self):
        return f"Ваш текущий баланс: {self.balanсe}"
    
    def main(self):
        while True:
            print("1 - Зарегистрироваться  \n2 - Пополнить баланс  \n3 - Снять деньги \n4 - Проверить баланс \n5 - Выйти ")
            command = int(input("Выберите действие: "))
            if command ==1: 
                print("Зарегистрироваться")
                name = input("Введите Ваше имя: ")
                surname = input("Введите Вашу фамилию: ")
                age = int(input("Введите Ваш возраст: "))
                email = input("Введите Вашу почту: ")
                print("Вы успешнго прошли регистрацию!")
                self.registr(name,surname, age, email)
            elif command == 2:
                if self.email:
                    print("Пополните баланс")
                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                else:
                    print("Зарегистрируйтесь ")
            elif command == 3:
                if self.email:
                    print("Снять деньги")
                    amount = int(input("Введите сумму: "))
                    if amount > self.balance:
                        print('Недостаточно средств для снятия денег!')
                        break
                    else:
                        self.minus(amount)
            elif command ==4:
                print(self.balance)
                
                        
            elif command == 5:
                break
            else:
                print("1 - Зарегистрироваться  \n2 - Пополнить баланс  \n3 - Снять деньги \n4 - Проверить баланс \n5 - Выйти ")
                command = int(input("Выберите действие: "))


bank = Bank()
bank.main()
   


     