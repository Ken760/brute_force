def simple_strategy(login_generator, password_generator, query):
    """
    :param login_generator: object wint generate() method
    :param password_generator: object wint generate() method
    :param query: function(login, password) -> bool
    """
    print('Start simple_strategy with params:', login_generator, password_generator, query)

    login = login_generator.generate()
    if login is None:
        return

    while True:
        password = password_generator.generate()
        if password is None:
            return

        if query(login, password):
            print('SUCCESS', login, password)
            return


def login_then_password_strategy(login_generator, password_generator, query, password_limit=1000):
    """
    :param login_generator: object wint generate() method
    :param password_generator: object wint generate() method
    :param query: function(login, password) -> bool
    :param password_limit: int, passwords per login
    """
    print('Start login_then_password_strategy with params:',
          login_generator, password_generator, query, password_limit)

    while True:
        login = login_generator.generate()
        if login is None:
            break

        password_generator.reset()
        for i in range(password_limit):
            password = password_generator.generate()
            if password is None:
                break

            if query(login, password):
                print('SUCCESS', login, password)
                break


def password_then_login_strategy(login_generator, password_generator, query,
                                 login_limit=1000, password_limit=1000):
    """
    :param login_generator: object wint generate() method
    :param password_generator: object wint generate() method
    :param query: function(login, password) -> bool
    :param login_limit: int, logins per password
    :param password_limit: int, passwords limit
    """
    print('Start password_then_login_strategy with params:',
          login_generator, password_generator, query, login_limit, password_limit)

    succeed_logins = set()

    for i in range(password_limit):
        password = password_generator.generate()
        if password is None:
            break

        for j in range(login_limit):
            login = login_generator.generate()
            if login is None:
                break

            if login not in succeed_logins and query(login, password):
                print('SUCCESS', login, password)
                succeed_logins.add(login)




