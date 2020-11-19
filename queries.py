from time import sleep

import requests


def request_local_sever(login, password):
    """Check if (login, password) valid for 'site'"""
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200


def request_local_sever_protected(login, password):
    try:
        response = requests.post('http://127.0.0.1:5000/auth',
                                 json={'login': login, 'password': password})
        return response.status_code == 200
    except:
        sleep(1)
        response = requests.post('http://127.0.0.1:5000/auth',
                                 json={'login': login, 'password': password})
        return response.status_code == 200



