""" Модуль описывающий логику загрузки страниц """
from src.request_handler import SafeRequest

def fetch_page(url) -> str | None:
    """ Функция получения текста кода страницы """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/144.0.0.0 YaBrowser/26.3.0.0 Safari/537.36'
    }
    safe_request = SafeRequest(url, headers)
    if safe_request:
        result = safe_request.request_handler()
        return result.text
    return None