import csv
import random
import os
import sys


NUM_ROWS = 50


COLUMNS = ['id', 'title', 'author', 'genre', 'year','pages', 'read']

def generate_row(rid):
    titles = [
        'Унесенные ветром', "Гарри Поттер и философский камень","Преступление и наказание","Мастер и Маргарита","Война и мир", "Вий", "Отцы и дети", "Гранатовый браслет", "Капитанская дочка", "Собачье сердце","Горе от ума", "Евгений Онегин", "451 градус по Фаренгейту"]
    authors = [ "Маргарет Митчелл", "Джоан Роулинг", "Федор Достоевский", "Михаил Булгаков", "Лев Толстой", "Николай Гоголь", "Иван Тургенев", "Александр Куприн", "Михаил Булгаков", "Александр Грибоедов", "Александр Пушкин", "Рэй Брэдбери"]
    genres = ["Роман", "Фэнтези", "Классика", "Повесть", "Фантастика","Комедия"]

    return {
        'id':rid,
        'title': random.choice(titles),
        'author': random.choice(authors),
        'genre': random.choice(genres),
        'year': random.randint(1800, 2024),
        'pages': random.randint(100, 1200),
        'read': random.choice(["Да", "Нет"])

    }
def main ():
    OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    rows = [generate_row(i) for i in range(1,NUM_ROWS+1)]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f'Создано {NUM_ROWS} книг в {OUTPUT_FILE}')

if __name__ == '__main__':
    main()