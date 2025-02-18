def total_salary(path: str) -> tuple[int | None, float | None]:
    """
    Функція аналізує файл, вираховує загальну та середню заробітні плати
    :param path: шлях до текстового файлу
    :return: кортеж із двох чисел: загальна сума зарплат і середня заробітна плата
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            my_list = [el.strip() for el in file.readlines() if el.strip()]

        if not my_list:
            return None, None

        persons_count = len(my_list)
        total_salaries = sum(int(el.split(',')[1]) for el in my_list)
        avg_salary = total_salaries / persons_count
        return total_salaries, avg_salary

    except (FileNotFoundError, UnicodeDecodeError, OSError, ValueError) as err:
        print('Нажаль, файл або відсутній або пошкоджений: {}'.format(err))
        return None, None

