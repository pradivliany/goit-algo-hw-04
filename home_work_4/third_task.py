import colorama
import sys
from pathlib import Path

def main() -> None:
    """
    Головна функція, в якій відбувається обробка аргументів командного рядка, та виклик функції
    для рекурсивного обходу директорії
    :return: None
    """
    try:
        parse_path = Path(sys.argv[1])

        def parse_folder(path: Path, space: str = '') -> None:
            """
            Рекурсивно обробляє файли та директорії в шляху path
            :param path: шлях до директорії
            :param space: відступ для вкладених елементів
            :return: None
            """
            for element in path.iterdir():
                if element.is_dir():
                    print(f'{space}{colorama.Fore.BLUE}{element.name}/{colorama.Fore.RESET}')
                    parse_folder(element, space + ' '*4)
                if element.is_file():
                    print(f'{space}{colorama.Fore.YELLOW}{element.name}{colorama.Fore.RESET}')

        parse_folder(parse_path)

    except (ValueError, IndexError, FileNotFoundError, PermissionError, OSError) as err:
        print('Виникла помилка: {}'.format(err))



if __name__ == '__main__':
    main()

