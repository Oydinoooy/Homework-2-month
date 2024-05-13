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
        self.balanse = 0
        self.props = None
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name 
        self.surname = surname
        self.age = age
        self.email = email
        cursor.execute(f"""INSERT INTO customs (name, surname, age, email, balanse, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}', 0, 0, True);""")
        connect.commit()

    def deposit(self, amount):
        cursor.execute(f"""UPDATE customs SET balanse = balanse + {amount} WHERE email = '{self.email}'""")
        connect.commit()
        self.balanse += amount 

    def minus(self, amount):
        cursor.execute(f"""UPDATE customs SET balanse = balance - {amount} WEHER email = '{self.email}'""")
        connect.commit()
        if amount > self.balanse:
            print("Извините, но на счету не осталось денег!")
        
        else:
            self.balanse -= amount
            print(f"Вы сняли {amount} \nВаш баланс {self.balanse}")


     