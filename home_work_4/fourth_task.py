def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'


def show_phone(args, contacts):
    name = args[0]
    return contacts[name] if name in contacts else "Ім'я не знайдено"


def show_all(contacts):
    return '\n'.join(f'{name} -> {value}' for name, value in contacts.items()) or 'Контактів немає'


def main():
    contacts = dict()
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can i help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
