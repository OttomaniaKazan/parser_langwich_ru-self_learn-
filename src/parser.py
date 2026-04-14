""" Модуль извлечения данных со страниц """
from bs4 import BeautifulSoup
from src.fetcher import fetch_page

def sections_parse() -> dict:
    url = 'https://langwitch.ru/wordsets/'
    data_text = fetch_page(url)
    soup = BeautifulSoup(data_text, 'html.parser')
    sections = soup.find('div', class_='wordsets_card').find_all('a', recursive=False)
    sections_dict = {}
    for section in sections:
        all_text = section.get_text(strip=True)
        attr_span = section.find('span').get_text()
        clear_text = all_text.replace(attr_span, "")
        url_attr = section.get('href')
        clear_url_attr = url_attr.replace('/wordsets/', '')
        sections_dict[clear_text] = clear_url_attr
    return sections_dict

def parse_section(section) -> dict:
    new_url = f'https://langwitch.ru/wordsets/{section}'
    data_text = fetch_page(new_url)
    soup = BeautifulSoup(data_text, 'html.parser')
    sections = soup.find_all('div', class_='word_row')
    ru_en_words = {}
    for section in sections:
        text_en = section.find('div', class_='word_row_en').get_text(strip=True)
        erase_text_en = section.find('div', class_='word_row_transcription').get_text()
        clear_text_en = text_en.replace(erase_text_en, '')
        text_ru = section.find('div', class_='word_row_ru').get_text(strip=True).capitalize()
        ru_en_words[text_ru] = clear_text_en
    return ru_en_words

def full_parser() -> dict:
    all_dict = {}
    sections = sections_parse()
    for category, section in sections.items():
        all_dict[category] = parse_section(section)
    return all_dict