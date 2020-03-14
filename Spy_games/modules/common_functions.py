from modules.config import ACCESS_TOKEN, VERSION

import requests
import time

# Функция получения ответа от API VK в виде json-а.

def get_response_json(request, params):
    try:
        response = requests.get(request, params, timeout = (3.05, 10)) 
    except requests.exceptions.ConnectTimeout:
        print('Ошибка ConnectTimeout')
    except requests.exceptions.ReadTimeout:
        print('Ошибка ReadTimeout')
    else:
        print('-' * 50)
        response_json = response.json()
        return response_json

if __name__ == "__main__":
    pass