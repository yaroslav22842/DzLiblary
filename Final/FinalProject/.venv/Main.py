
#exchange_rate = 0
#Request = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
#if Request.status_code == 200:
#    soup = BeautifulSoup(Request.text, features="html.parser")
#
#
#    table = soup.find("table", {"id": "exchangeRates"})
#
#
#    rows = table.find_all("tr")
#
#
#    for row in rows:
#        cells = row.find_all("td")
#        if cells and cells[1].text == "USD":
#            currency_name = cells[3].text.strip()
#            exchange_rate = cells[4].text.strip().replace(",", ".")
#            exchange_rate = float(exchange_rate)
#            print(f"Курс {currency_name} (USD): {exchange_rate}")
#            break
#else:
#    print("Ошибка при получении данных")
#
#Money = input("Сумма: ")
#Money = float(Money)
#Money = Money * exchange_rate
#print(Money)


#------------------------------------------------------------------------------------



#
#con = sqlite3.connect("itstep_db.sl3")
#cur = con.cursor()
#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("INSERT INTO first_table (name) VALUES ('sara');")
#cur.execute("UPDATE first_table SET name='john' WHERE rowid=3;")
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
#
#con.commit()
#res = cur.fetchall()
#print(res)
#print(con)
#print(cur)
#con.close()
#
#
#
#
# Примеры по которым я делал сверху
# Некоторую ифнормацию я позаимствовал из интернета
# Делать проект в некоторых местах помогал chatGPT
# Трудне всего было сделать систему для базы данных
# Ниже я покажу что и как работает
#

#Импорт библиотек
import requests
from bs4 import BeautifulSoup
import sqlite3


def run(): #Функция запуска программы
    db_manager = DatabaseManager()
    web_parser = WebParser()
    user_interface = UserInterface(db_manager, web_parser)

    while True: #Функционал интерфейса
        choice = user_interface.show_main_menu()
        if choice == '1':
            user_interface.add_sites()
        elif choice == '2':
            user_interface.clear_database()
        elif choice == '3':
            query = user_interface.get_search_query()
            results = web_parser.search(db_manager.get_sites(), query)
            user_interface.display_results(results)
        elif choice == '4':
            break

    db_manager.close()
class DatabaseManager: #Класс в котором храняться все функции для взаймодействия с БД
    def __init__(self, db_name='sites.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self): #Создать таблицу
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY,
                url TEXT NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()

    def add_site(self, url): #Добавить сайт
        try:
            self.cursor.execute('INSERT INTO sites (url) VALUES (?)', (url,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Сайт {url} уже существует в базе данных.")

    def clear_sites(self): #Убрать сайты из БД
        self.cursor.execute('DELETE FROM sites')
        self.conn.commit()

    def get_sites(self): #Получить сайты из БД
        self.cursor.execute('SELECT url FROM sites')
        return [row[0] for row in self.cursor.fetchall()]

    def close(self): #Закрыть подключение
        self.conn.close()
class WebParser: #Класс для парсинга
    def search(self, sites, query): # функция для поиска по ключевому слову
        results = {}
        for site in sites:
            content = self.fetch_content(site)
            if content:  # Проверка что контент не пустой
                count = content.lower().count(query.lower())
                if count > 0:
                    results[site] = count
            else:
                print(f"Контент для {site} не загружен.")
        return sorted(results.items(), key=lambda x: x[1], reverse=True)


    def fetch_content(self, url): #Проверка насколько успешно подкоючились к сайту
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as e:
            print(f"Ошибка при загрузке {url}: {e}")
        return ""


class UserInterface: #Класс в котором храниться сам интерфейс
    def __init__(self, db_manager, web_parser):
        self.db_manager = db_manager
        self.web_parser = web_parser

    def show_main_menu(self): #Тут показываеться интерфейс
        print("1. Добавить сайт")
        print("2. Очистить базу данных")
        print("3. Поиск")
        print("4. Выход")
        return input("Выберите действие: ")

    def add_sites(self): #Здесь вызывааеться функция для добавления сайтов
        url = input("Введите URL сайта: ")
        self.db_manager.add_site(url)

    def clear_database(self): #Это для очистки всей базы данных
        self.db_manager.clear_sites()
        print("База данных очищена.")

    def get_search_query(self): #Запросы
        return input("Введите поисковый запрос: ")

    def display_results(self, results): #Тут показываються результаты
        if results:
            print("Результаты поиска:")
            for site, count in results:
                print(f"{site}: {count} обьекта по зпросу")
        else:
            print("Ничего не найдено.")

run()
db_manager.clear_sites()




