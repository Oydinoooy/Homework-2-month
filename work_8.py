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
