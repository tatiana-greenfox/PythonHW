from pprint import pprint

import requests

# API_ID = '7309299'
access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

# user_screen_name = 'eshmargunov'
# user_id = '171691064'

def get_response(request, params):
    response = requests.get(request, params) 
    response_json = response.json()
    items_list = response_json['response']['items']
    return items_list

class User:
    def input_user_name(self):
        # self.user_name = input('Введите имя или id пользователя: ')
        self.user_name = 'eshmargunov'
        return self.user_name

    def get_user_id(self):
        self.user_name = self.input_user_name()

        if self.user_name.isdigit() == True:
            self.user_id = self.user_name
            return self.user_id
        else:
            self.screen_name = self.user_name

            self.params = {
                'access_token': access_token,
                'v': version,
                'user_ids': self.screen_name
            }

            response = requests.get('https://api.vk.com/method/users.get' , self.params) 
            response_json = response.json()
        
            for value in response_json['response']:
                self.user_id = value['id']
            return self.user_id

    def get_friends_list(self, user_id):            
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': user_id,
            'order': 'hints', 
            'fields': 'deactivated'
            }

        self.request = 'https://api.vk.com/method/friends.get'

        return get_response(self.request, self.params)

        # response = requests.get('https://api.vk.com/method/friends.get' , self.params)
        # response_json = response.json()
        # items_list = response_json['response']['items']
        # return items_list
    
    def get_groups_list(self, user_id):
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': user_id,
            'extended': '1',
            'count': '200',
            'fields': ['id', 'name', 'members_count']
        }

        self.request = 'https://api.vk.com/method/users.getSubscriptions'

        return get_response(self.request, self.params)

        # response = requests.get('https://api.vk.com/method/users.getSubscriptions' , self.params) 
        # response_json = response.json()
        # items_list = response_json['response']['items']
        # return items_list

class Group:
    pass

if __name__ == "__main__":
    user = User()
    user_id = user.get_user_id()

    user_groups = user.get_groups_list(user_id)
    user_groups_id_list = []

    user_friends = user.get_friends_list(user_id)
    user_friends_id_list = []

    # получение списка id друзей пользователя
    for friend in user_friends:
        if (friend.get('deactivated') == 'deleted') or (friend.get('deactivated') == 'banned'):
            pass
        else:
            user_friends_id_list.append(friend['id'])

    # получение списка id групп пользователя
    for group in user_groups:
        user_groups_id_list.append(group['id'])

    # преобразование списка в множество   
    user_groups_id_set = set(user_groups_id_list)

    # создание объекта для каждого друга пользователя и получение списка групп для каждого друга
    # Вопрос: правильно ли Я получаю список групп для каждого друга? Если в конце не поставить break выдается ошибка keyerror 'response'
    friends_groups_list = []
    friends_groups_id_list = []

    for friend_id in user_friends_id_list:
        friend = User()
        friends_groups_list = friend.get_groups_list(friend_id)
        break 

    for group in friends_groups_list:
        friends_groups_id_list.append(group['id'])
    
    # получение множества групп, в которые входит пользователь, но не входит никто из его друзей
    friends_groups_id_set = set(friends_groups_id_list)

    print(user_groups_id_set.difference(friends_groups_id_set))
    

    

   
