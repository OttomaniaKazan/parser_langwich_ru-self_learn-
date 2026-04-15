""" Модуль извлечения данных со страниц """
from bs4 import BeautifulSoup
from src.fetcher import fetch_page

def sections_parse() -> dict:
    """ Получение словаря с категориями слов и индекса html-страницы для нее"""

    url = 'https://langwitch.ru/wordsets/'
    data_text = fetch_page(url)
    soup = BeautifulSoup(data_text, 'html.parser')
    sections = soup.find('div', class_='wordsets_card').find_all('a',
                                                            recursive=False)
    print(f'Найдено всего {len(sections)} категорий')
    sections_dict = {}
    for section in sections:
        all_text = section.get_text(strip=True)
        attr_span = section.find('span').get_text()
        clear_text = all_text.replace(attr_span, "")
        url_attr = section.get('href')
        clear_url_attr = url_attr.replace('/wordsets/', '')
        sections_dict[clear_text] = clear_url_attr
        print(f'Добавлена категория {clear_text}.\n '
              f'Cсылка на категорию https://langwitch.ru/wordsets/{clear_url_attr}')
    return sections_dict

def normalize_key(text) -> str:
    """ Преобразуем ключ максимум до двух слов """
    text_list = text.split()
    normal_size = text_list[:3]
    normal_text = ' '.join(normal_size).strip().capitalize()
    return normal_text

def parse_section(category) -> dict:
    """ Получение словаря {Ru:En} для каждой категории """
    new_url = f'https://langwitch.ru/wordsets/{category}'
    data_text = fetch_page(new_url)
    soup = BeautifulSoup(data_text, 'html.parser')
    sections = soup.find_all('div', class_='word_row')
    ru_en_words = {}
    count = 0
    for section in sections:
        text_en = section.find('div', class_='word_row_en').get_text(strip=True)
        erase_text_en = section.find('div', class_='word_row_transcription').get_text()
        clear_text_en = text_en.replace(erase_text_en, '')
        text_ru = section.find('div', class_='word_row_ru').get_text(strip=True).capitalize()
        normal_text_ru = normalize_key(text_ru)

        # Убираем дубликаты ключей без учета категорий
        key_seen = set()
        if normal_text_ru not in key_seen:
            ru_en_words[normal_text_ru] = clear_text_en
            key_seen.add(normal_text_ru)
            count += 1

    print(f'Найдено {count} слов.')
    return ru_en_words

def full_parser() -> dict:
    """ Получение полного словаря слов, разбитого по категориям"""

    all_dict = {}
    sections = sections_parse()
    for category, section in sections.items():
        all_dict[category] = parse_section(section)
        print(f'Добавлен словарь для категории {category}')
    print('Парсинг выполнен!')
    return all_dict