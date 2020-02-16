from pprint import pprint

import requests, time, json

# API_ID = '7309299'
access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

# user_screen_name = 'eshmargunov'
# user_id = '171691064'

def requests_get(request, params):
    response = requests.get(request, params) 
    response_json = response.json()
    items_list = response_json['response']['items']
    return items_list

class User:
    def input_user_name(self):
        self.user_name = input('Введите имя или id пользователя: ')
        # self.user_name = 'eshmargunov'
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

        return requests_get(self.request, self.params)
    
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

        return requests_get(self.request, self.params)

class Group:
    def get_info_group(self, groups_id_list):
        self.params = {
                'access_token': access_token,
                'v': version,
                'group_id': group_id,
                'fields': 'members_count'
            }

        response = requests.get('https://api.vk.com/method/groups.getById' , self.params) 
        response_json = response.json()
        group_dict = {}

        for group in response_json['response']:
            group_dict = {
                    'name': group['name'],
                    'gid': group['id'],
                    'members_count': group['members_count']
                }
        return group_dict


if __name__ == "__main__":
    user = User()
    user_id = user.get_user_id()
    user_groups = user.get_groups_list(user_id)
    user_friends = user.get_friends_list(user_id)

    # получение списка id друзей пользователя,
    # если у друга нет пометки заблокированн или удален и при этом пользователь может просматривать информацию о нем,
    # тогда вносим id друга в список
    user_friends_id_list = []

    for friend in user_friends:
        if (friend.get('deactivated') == 'deleted') or (friend.get('deactivated') == 'banned') or ((friend.get('is_closed') == '1') and (friend.get('can_access_closed') == '0')):
            pass
        else:
            user_friends_id_list.append(friend['id'])

    # получение списка id групп пользователя
    # создаем множество, которое будет содержать id групп пользователя
    user_groups_id_set = set()

    for group in user_groups:
        user_groups_id_set.add(group['id'])

    # создание объекта для каждого друга пользователя и получение списка групп для каждого друга
    friend = User()
    friends_groups_list = []
    all_friends_groups_list = []
    
    print('-' * 10)
    for friend_id in user_friends_id_list:  
        try:
            friends_groups_list = friend.get_groups_list(friend_id)
            all_friends_groups_list.append(friends_groups_list)
        except Exception:
            time.sleep(2)
            print('-' * 10)

    friends_groups_id_set = set()

    for group_list in all_friends_groups_list:
        for group in group_list:
            friends_groups_id_set.add(group['id'])

    difference_groups = user_groups_id_set.difference(friends_groups_id_set)
    group = Group()
    group_list = []

    for group_id in difference_groups:
        print('-' * 10)
        try:
            group_info = group.get_info_group(group_id)
            group_list.append(group_info)
        except Exception:
            time.sleep(2)
            print('-' * 10)
    
    with open('groups.json' , 'w', encoding='utf-8') as json_file:
        json.dump(group_list, json_file, ensure_ascii=False)