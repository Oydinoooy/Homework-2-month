import sqlite3
import random

connect = sqlite3.connect('game_2.db')
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               fullname TEXT, 
               score INT
               )
""")

def add_player(fullname):
    cursor.execute("INSERT INTO players (fullname, score) VALUES (?, 0)", (fullname,))
    connect.commit()
    print("Игрок {} сохранен.".format(fullname))

def update_score(fullname, score):
    cursor.execute("UPDATE players SET score = ? WHERE fullname = ?", (score, fullname))
    connect.commit()

def get_score(fullname):
    cursor.execute("SELECT score FROM players WHERE fullname = ?", (fullname,))
    score = cursor.fetchone()
               
    if score:
        return score[0]
    else:
        return None 
    
def get_gametable():
    cursor.execute("SELECT fullname, score FROM players ORDER BY score DESC LIMIT 30")
    gametable = cursor.fetchall()
    print("Таблица лидеров: ")
    for i, (fullname, score) in enumerate(gametable, 1):
        print("{}. {}: {}".format(i, fullname, score))

fruits = ("Ананас", "Мандарин", "Киви", "Лимон", "Гранат", "Яблоко", "Грейпфрут", "Персик", "Айва", "Виноград", "Нектарин")

def play_game(fullname):
    print("Рады Вас видеть в нашей игры, {}!".format(fullname))
    fruit_word = random.choice(fruits).lower()
    word_mine = '_' * len(fruit_word)
    tries = 0
    guessed_letters = set()

    while True:
        guess = input("Попробуйте угадать спрятанный фрукт или введите слово целиком: ").lower()
        tries += 1

        if guess:
            if guess in guessed_letters:
                print("Вы уже вводили эту букву или слово!")
                continue

            guessed_letters.add(guess)

            if len(guess) > 1:
                if guess == fruit_word:
                    print("Поздравляем! Вы угадали слово '{}' за {} попыток.".format(fruit_word, tries))
                    update_score(fullname, get_score(fullname) + 1)
                    break
                else:
                    print("Неверно. Попробуйте еще раз или введите букву.")
                    continue

            if guess in fruit_word:
                new_word = ''
                for i in range(len(fruit_word)):
                    if guess == fruit_word[i]:
                        new_word += guess
                    else:
                        new_word += word_mine[i]
                word_mine = new_word
                print('\nВерно. Текущий вид слова: ', word_mine)
            else:
                print("Такой буквы нет")
        else:
            print('Ничего не введено, попробуйте снова')

        if word_mine == fruit_word:
            print("Поздравляем! Вы угадали слово '{}' за {} попыток.".format(fruit_word, tries))
            update_score(fullname, get_score(fullname) + 1)
            break

def main():
    while True:
        print("1. Начать")
        print("2. Таблица лидеров")
        print("3. Выйти из игры")
        choice = input("Выберите следующий шаг: ")

        if choice == "1":
            fullname = input("Введите вашу фамилию и имя: ")
            if not get_score(fullname):
                add_player(fullname)
            play_game(fullname)
        
        elif choice == "2":
            get_gametable()

        elif choice == "3":
            print("Ждем Вас снова!")
            break
        else:
            print("Неправильный ввод данных. Попробуйте ещё раз!")

main()

"""git add
git commit 
git push """