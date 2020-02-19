import requests
import time
import json

access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

def get_response_list(request, params):
    response = requests.get(request, params) 
    response_json = response.json()
    response_list = response_json['response']
    return response_list   

def get_user_id(user_name):
    if user_name.isdigit() == True:
        user_id = user_name
        return user_id
    else:
        screen_name = user_name

        params = {
            'access_token': access_token,
            'v': version,
            'user_ids': screen_name
        }

        request = 'https://api.vk.com/method/users.get'
        response_list = get_response_list(request, params)
    
        for value in response_list:
            user_id = value['id']
        return user_id  

class User:
    def get_friends_list(self, user_id):            
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': user_id,
            'order': 'hints', 
            'fields': 'deactivated'
            }

        self.request = 'https://api.vk.com/method/friends.get'

        response_list = get_response_list(self.request, self.params)
        items_list = response_list['items']

        return items_list
    
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

        response_list = get_response_list(self.request, self.params)
        items_list = response_list['items']

        return items_list

class Group:
    def get_info_group(self, group_id):
        self.params = {
                'access_token': access_token,
                'v': version,
                'group_id': group_id,
                'fields': 'members_count'
            }

        self.request = 'https://api.vk.com/method/groups.getById'
        response_list = get_response_list(self.request, self.params)    

        group_dict = {}

        for group in response_list:
            group_dict = {
                    'name': group['name'],
                    'gid': group['id'],
                    'members_count': group['members_count']
                }
        return group_dict

def writing_groups_in_json(groups, path):
    group_list = []

    for group_id in groups:
        try:
            group_info = group.get_info_group(group_id)
        except Exception:
            print('-' * 10)
            time.sleep(2)
        else:
            print('-' * 10)
            group_list.append(group_info)
    
    with open(path , 'w', encoding='utf-8') as json_file:
        json.dump(group_list, json_file, ensure_ascii=False)

if __name__ == "__main__":
    #тестовый пользователь: 'eshmargunov' или '171691064'
    user_name = input('Введите имя или id пользователя: ')
    # user_name = 'eshmargunov'
    user_id = get_user_id(user_name)

    user = User()

    user_friends = user.get_friends_list(user_id)

    # получение id групп пользователя
    user_groups_id_set = set()
    try:
        user_groups = user.get_groups_list(user_id)
    except Exception:
        print('-' * 10)
        time.sleep(2)
    else:
        print('-' * 10)
        for group in user_groups:
            user_groups_id_set.add(group['id'])
   
    # получение списка id друзей пользователя,
    # если у друга нет пометки заблокированн или удален и при этом пользователь может просматривать информацию о нем,
    # тогда вносим id друга в список
    
    friends_id_list = []

    for friend in user_friends:
        if (friend.get('deactivated') == 'deleted') or (friend.get('deactivated') == 'banned') or ((friend.get('is_closed') == '1') and (friend.get('can_access_closed') == '0')):
            pass
        else:
            friends_id_list.append(friend['id'])

    # получение списка групп для каждого друга
    friend = User()

    friend_groups_list = []
    friends_groups_list = []
  
    for friend_id in friends_id_list:  
        try:
            friend_groups_list = friend.get_groups_list(friend_id)
        except Exception:
            print('-' * 10)
            time.sleep(2)
        else:
            print('-' * 10)
            friends_groups_list.append(friend_groups_list)
           
    # получение id групп друзей пользователя
    friends_groups_id_set = set()

    for group_list in friends_groups_list:
        for group in group_list:
            friends_groups_id_set.add(group['id'])

    difference_groups = user_groups_id_set.difference(friends_groups_id_set)

    group = Group()

    writing_groups_in_json(difference_groups, 'groups_2.json')