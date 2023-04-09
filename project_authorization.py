# Регистрация и авторизация
FILENAME = 'log.txt'
REGISTER = 1
AUTHORIZED = 2


def create_file():  # для создания файла при запуске
    with open(FILENAME, 'w+', encoding='utf-8'):
        return


def read_file():  # для чтения файла
    with open(FILENAME, encoding='utf-8') as f:
        return f.readlines()


def write_file(login, password):  # для записи в файл
    with open(FILENAME, 'a+', encoding='utf-8') as f:
        f.write(''.join([login, ';', password, '\n']))
        print('Данные успешно записаны!')


def choice_command(command):  # выбор команды (регистрация или авторизация)
    login, password = log_pass_input()
    if command == REGISTER:
        account_register(login, password)
    elif command == AUTHORIZED:
        account_authorize(login, password)


def log_pass_input():  # ввод логина и пароля
    login = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    # проверка на длину логина и пароля
    if not (3 < len(login) < 21) or not (4 < len(password) < 33):
        print('Имя пользователя или пароль слишком короткие!')
        return None, None
    return login, password


def check_login(login):  # проверка логина при регистрации
    # проверка на наличие такого пользователя в БД
    for line in read_file():
        log_file_read = line.split(';')[0]
        if login == log_file_read:
            print('Такое имя пользователя уже существует')
            print('Придумайте другой, либо авторизуйтесь')
            return True
    return False


def account_register(login, password):  # регистрация

    # проверка логина на наличие в БД
    if check_login(login):
        return
    # запись данных в БД
    write_file(login, password)


def log_pass_verification(login, password):

    for line in read_file():  # проверка на совпадения в БД
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
        print('Вы переведены в главное меню')


def account_authorize(login, password):  # авторизация

    log_pass_verification(login, password)


def main():
    create_file()
    print('Добро пожаловать!')
    print('Хотите зарегистрироваться или авторизоваться?')
    while True:
        try:
            print('Нажмите 1 для регистрации и 2 для авторизации')
            command = int(input('Введите цифру: '))
            if command not in [1, 2]:
                raise ValueError
            choice_command(command)
        except ValueError:
            print('Ошибка ввода данных!')


if __name__ == '__main__':
    main()
