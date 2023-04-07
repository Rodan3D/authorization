# Регистрация и авторизация
FILENAME = 'log.txt'


def create_file():  # для создания файла при запуске
    with open(FILENAME, 'w', encoding='utf-8'):
        return


def read_file():  # для чтения файла
    with open(FILENAME, encoding='utf') as f:
        return f.readlines()


def write_file(login, password):  # для записи в файл
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write(''.join([login, ";", password, '\n']))


def choise_command(command):
    register = 1
    authorized = 2
    if command == register:
        account_register()
    elif command == authorized:
        account_authorize()
    else:
        print('Введены неверные данные! Повторите попытку!')


def log_pass_input():
    login = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    return login, password


def account_register():
    login, password = log_pass_input()
    # проверка на длину логина и пароля
    if not (3 < len(login) < 21) or not (4 < len(password) < 33):
        print('Имя пользователя или пароль слишком короткие!')
        return

    for line in read_file():  # проверка на наличие такого пользователя в БД
        log_file_read = line.split(';')[0]
        if login == log_file_read:
            print('Такое имя пользователя уже существует')
            print('Придумайте другой, либо авторизуйтесь')
            return

    write_file(login, password)
    print('Данные успешно записаны!')


def account_authorize():
    login, password = log_pass_input()
    lines = read_file()
    if not lines:
        print('В базе данных такой пользователь не найден!')
        print('Вы переведены в меню регистрации')
        account_register()
    else:
        for line in lines:  # проверка на совпадения в БД
            log_file_read = line.split(';')[0]  # логин
            pass_file_read = line.rstrip('\n').split(';')[1]  # пароль

            if login == log_file_read and password == pass_file_read:
                print('Авторизация успешна!')
                break

            elif login == log_file_read and password != pass_file_read:
                print('Введен неверный пароль! Повторите попытку!')
                break

        else:
            print('В базе данных такой пользователь не найден!')
            print('Вы переведены в меню регистрации')
            account_register()


def main():
    create_file()
    print('Добро пожаловать!')
    print('Хотите зарегистрироваться или авторизоваться?')
    while True:
        try:
            print('Нажмите 1 для регистрации и 2 для авторизации')
            command = int(input('Введите цифру: '))
            choise_command(command)
        except ValueError:
            print('Ошибка типа данных!')


if __name__ == '__main__':
    main()
