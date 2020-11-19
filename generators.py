class BruteForceGenerator:
    def __init__(self, alphabet='0123456789abcdefgihjklmnopqrstuvwxyz'):
        self.alphabet = alphabet
        self.base = len(self.alphabet)

        self.length = 0
        self.counter = 0

    def reset(self):
        self.length = 0
        self.counter = 0

    def generate(self):
        password = ''

        temp = self.counter
        while temp > 0:
            rest = temp % self.base
            temp = temp // self.base
            password = self.alphabet[rest] + password

        while len(password) < self.length:
            password = self.alphabet[0] + password

        if password == self.alphabet[-1] * self.length:
            self.length += 1
            self.counter = 0
        else:
            self.counter += 1

        return password


class ListGenerator:
    def __init__(self, tokens):
        self.tokens = tokens
        self.counter = 0

    def reset(self):
        self.counter = 0

    def generate(self):
        if self.counter < len(self.tokens):
            password = self.tokens[self.counter]
            self.counter += 1
            return password


class PopularPasswordsGenerator(ListGenerator):
    def __init__(self, filename='popular-passwords.txt'):
        with open(filename) as tokens_file:
            tokens = tokens_file.read().split('\n')
        super().__init__(tokens=tokens)







