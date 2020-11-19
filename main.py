import queries
import generators
import strategies

strategies.simple_strategy(
    login_generator=generators.PopularPasswordsGenerator(),
    password_generatro=generators.BruteForceGenerator(),
    query=queries.request_local_sever
)
