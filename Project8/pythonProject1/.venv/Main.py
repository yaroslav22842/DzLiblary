import requests
from bs4 import BeautifulSoup
exchange_rate = 0
Request = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if Request.status_code == 200:
    soup = BeautifulSoup(Request.text, features="html.parser")


    table = soup.find("table", {"id": "exchangeRates"})


    rows = table.find_all("tr")


    for row in rows:
        cells = row.find_all("td")
        if cells and cells[1].text == "USD":
            currency_name = cells[3].text.strip()
            exchange_rate = cells[4].text.strip().replace(",", ".")
            exchange_rate = float(exchange_rate)
            print(f"Курс {currency_name} (USD): {exchange_rate}")
            break
else:
    print("Ошибка при получении данных")

Money = input("Сумма: ")
Money = float(Money)
Money = Money * exchange_rate
print(Money)

