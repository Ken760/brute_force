import requests

urls =['https://vk.com/login', '']
count_requests = 100

for url in urls:
    print(url)
    for j in range(count_requests):
        response = requests.get(url)
        print(response.status_code)

print('finish')