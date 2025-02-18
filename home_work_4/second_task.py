def get_cats_info(path: str) -> list[dict]:
    """
    Функція працює з файлом, обробляє дані.
    :param path: шлях до текстового файлу
    :return: список словників, де кожен словник містить інформацію про одного кота
    """
    result = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:  # пробігаємось по кожному рядку в файлі (спробував як альтернативу readlines())
                line = line.strip()  # забираємо символи нового рядка і пробіли
                cat_dict = dict()  # створюємо пустий словник для одного кота
                cat_id, cat_name, cat_age = line.split(',')  # отримуємо потрібну інформацію з рядка
                cat_dict['id'], cat_dict['name'], cat_dict['age'] = cat_id, cat_name, cat_age  # записуємо в словник
                result.append(cat_dict)  # словник вносимо в результуючий список
        return result

    except (FileNotFoundError, ValueError, OSError, UnicodeDecodeError) as err:
        print(f'Файл не знайдений або пошкоджений, помилка = {err}')
        return result
    