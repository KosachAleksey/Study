from bs4 import BeautifulSoup
import requests

url = "https://sochi1.ru/text/world/2025/05/05/75423095/?ysclid=mabdt4xii5310162036"

page = requests.get(url)

filterNews = []
allNews = []

# Использование правильного парсера ("html.parser")
soup = BeautifulSoup(page.text, "html.parser")

# Поиск первого элемента h2 на странице
title_tag = soup.find("h2")

# Если тег h2 существует, печатаем его текст
if title_tag:
    print(title_tag.text)
else:
    print("Заголовок не найден.")