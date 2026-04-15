Написано 2 функции в файл parser.py для нормализации вида ключей (не более 3х слов) и что бы не возникало конфликтов ключей при объединении всех разделов в единый словарь, в процессе парсинга на лету, не записывались повторные ключи, кроме первого.

функции:
```python
def normalize_key(text) -> str:
    """ Преобразуем ключ максимум до двух слов """
    text_list = text.split()
    normal_size = text_list[:3]
    normal_text = ' '.join(normal_size).strip().capitalize()
    return normal_text
```

```python
def check_duplicates(text) -> bool:
    """ Удаляем дубликаты ключей """
    key_seen = set()
    if text in key_seen:
        return True
    else:
        key_seen.add(text)
        return False
```