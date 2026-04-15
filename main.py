from src.parser import full_parser
from src.saver import save_to_json


def main():
    data = full_parser()
    save_to_json(data)

if __name__ == '__main__':
    main()