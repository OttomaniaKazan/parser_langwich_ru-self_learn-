from src import fetcher
from src.fetcher import fetch_page

url = 'https://langwitch.ru/wordsets/4/'

# Используемый заголовок
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                ' (KHTML, like Gecko) Chrome/144.0.0.0 YaBrowser/26.3.0.0 Safari/537.36'
}

page_text = fetch_page(url)
print(type(page_text))