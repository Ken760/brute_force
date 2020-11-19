import queries
import generators
import strategies

strategies.password_then_login_strategy(
    login_generator=generators.PopularPasswordsGenerator('popular-passwords.txt'),
    password_generator=generators.PopularPasswordsGenerator('popular-passwords.txt'),
    query=queries.request_local_sever
)

strategies.password_then_login_strategy(
    login_generator=generators.ListGenerator(['admin', 'test', 'test1']),
    password_generator=generators.PopularPasswordsGenerator('popular-passwords.txt'),
    query=queries.request_local_sever
)

strategies.simple_strategy(
    login_generator=generators.PopularPasswordsGenerator('popular-passwords.txt'),
    password_generator=generators.BruteForceGenerator(),
    query=queries.request_local_sever
)
