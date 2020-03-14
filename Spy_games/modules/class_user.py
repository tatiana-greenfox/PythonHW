from modules.config import ACCESS_TOKEN, VERSION
from modules.common_functions import get_response_json

import time

class User:

    def __init__(self, name):
        self.name = name

    # Функция получения id пользователя.
    # В ходе выполнения ф-ии осуществляется проверка является ли name строкой (ввод с клавиатуры) или числом,
    # если строка, то проводится еще одна проверка, если введенное имя содержит только цирфы, то считаем, что был введен id ползователя, 
    # если нет, то отправляем запрос к API VK для получения ползователького id.

    def get_user_id(self):
        if type(self.name) == str:
            if self.name.isdigit() == True:
                user_id = self.name
                return user_id
            else:
                params = {
                    'access_token': ACCESS_TOKEN,
                    'v': VERSION,
                    'user_ids': self.name
                }

                request = 'https://api.vk.com/method/users.get'
                response_json = get_response_json(request, params)
                
                for value in response_json['response']:
                    user_id = value['id']
                return user_id  
        else:
            user_id = self.name
            return user_id

    # Функция получения списка id групп пользователя.

    def get_groups_id_list(self):
        user_id = self.get_user_id()
        offset = 0

        params = {
            'access_token': ACCESS_TOKEN,
            'v': VERSION,
            'user_id': user_id,
            'extended': 0,
            'offset': offset,
            'count': 1000
        }

        request = 'https://api.vk.com/method/groups.get'

        response_json = get_response_json(request, params)
        groups_id_list = response_json['response']['items']

        while len(groups_id_list) < response_json['response']['count']:
            offset += 1000

            params = {
                'access_token': ACCESS_TOKEN,
                'v': VERSION,
                'user_id': user_id,
                'extended': 0,
                'offset': offset,
                'count': 1000
             }

            response_json = get_response_json(request, params) 
            time.sleep(0.35)

            groups_id_list.extend(response_json['response']['items'])

        return groups_id_list

    # Функция получения списка с расширенной информацией о друзьях пользователя.

    def get_friends_list(self):      
        user_id = self.get_user_id()

        params = {
            'access_token': ACCESS_TOKEN,
            'v': VERSION,
            'user_id': user_id,
            'order': 'hints', 
            'fields': 'deactivated'
            }

        request = 'https://api.vk.com/method/friends.get'

        response_json = get_response_json(request, params) 
        friends_list = response_json['response']['items']

        return friends_list

    # Функция получения списка id друзей пользователя.

    def get_friends_id_list(self):            
        friends_list = self.get_friends_list()
  
        friends_id_list = []

        for friend in friends_list:
            # Помещаем id друга в список, если он не помечен как "удаленный" или "заблокированный", и пользователь имет доступ к его данным. 
            if (friend.get('deactivated') != 'deleted') or (friend.get('deactivated') != 'banned') or ((friend.get('is_closed') != '1') and (friend.get('can_access_closed') != '0')):
                friends_id_list.append(friend['id'])
                
        return friends_id_list

if __name__ == "__main__":
    pass