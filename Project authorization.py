#Регистрация и авторизация
def create_file(filename):
    with open(filename, 'a+', encoding='utf-8') as f:
        pass


def chooise_comand(comand):
    register = 1
    authorized = 2
    if comand == register:
        account_register()
    elif comand == authorized:
        account_authorize()
    elif comand != register and comand != authorized:
        print('Введены неверные данные! Повторите попытку!')


def account_register():
    login = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    for i in login, password:                                               # проверка на длину логина и пароля
        if 3 < len(login) < 21 and 4 < len(password) < 33:
            continue
        else:
            print('Имя пользователя или пароль слишком короткие!')
            return

    with open('log.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:                                                  # проверка на наличие такого пользователя в БД
            log_file_read = line.split(';')[0]
            if login == log_file_read:
                print('Такое имя пользователя уже существует')
                print('Придумайте другой, либо авторизуйтесь')
                return
        else:
            f.write(''.join([login, ";", password, '\n']))
            print('Данные успешно записаны!')


def account_authorize():
    login = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    with open('log.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        if not lines:
            print('В базе данных такой пользователь не найден!')
            print('Вы переведены в меню регистрации')
            account_register()
        else:
            for line in lines:                                                  # проверка на совпадения в БД
                log_file_read = line.split(';')[0]  # логин
                pass_file_read = line.rstrip('\n').split(';')[1] # пароль

                if login == log_file_read and password == pass_file_read:
                    print('Авторизация успешна!')

                elif login == log_file_read and password != pass_file_read:
                    print('Введен неверный пароль! Повторите попытку!')


def main():
    filename = 'log.txt'
    create_file(filename)
    print('Добро пожаловать!')
    print('Хотите зарегистрироваться или авторизоваться?')
    while True:
        try:
            print('Нажмите 1 для регистрации и 2 для авторизации')
            comand = int(input('Введите цифру: '))
            chooise_comand(comand)
        except ValueError:
            print('Ошибка типа данных!')


if __name__ == '__main__':
    main()
