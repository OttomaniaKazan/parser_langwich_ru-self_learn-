""" Модуль сохранения в JSON """

import json
from pathlib import Path

def save_to_json(data) -> None:
    project_root = Path(__file__).resolve().parent.parent
    path_obj = project_root / 'data'
    # Создаем папку для хранения данных парсинга
    try:
        path_obj.mkdir(parents=True, exist_ok=True)
    except PermissionError as e:
        print(f"Нет прав на создание папки {path_obj}: {e}")
        return None
    except OSError as e:
        print(f"Ошибка файловой системы при создании {path_obj}: {e}")
        return None
    except Exception as e:
        print("Неожиданная ошибка при работе с директорией")
        return None

    filename = path_obj / 'vocabulary.json'

    # Записываем данные парсинга в файл
    with open(filename, 'w', encoding='utf-8') as f:
        try:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print(f'Файл {filename} успешно записан')
        except PermissionError as e:
            print(f"Нет прав на создание файла {f}: {e}")
            return None
        except OSError as e:
            print(f"Ошибка файловой системы при создании {f}: {e}")
            return None
        except UnicodeEncodeError as e:
            print(f"Ошибка кодировки при записи: {e}")
            return None
        except Exception as e:
            print("Неожиданная ошибка при работе с файлом")
            return None