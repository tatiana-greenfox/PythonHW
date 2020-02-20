import requests
import time
import json

access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

class User:
    def get_groups_id_list(self, user_id):
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': user_id,
            'extended': '1',
            'count': '1000'
        }

        self.request = 'https://api.vk.com/method/groups.get'

        response_json = get_response_json(self.request, self.params)
        items_list = response_json['response']['items']

        groups_id_list = []

        for group in items_list:
            groups_id_list.append(group['id'])
        
        return groups_id_list

    def get_friends_id_list(self, user_id):            
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': user_id,
            'order': 'hints', 
            'fields': 'deactivated'
            }

        self.request = 'https://api.vk.com/method/friends.get'

        response_json = get_response_json(self.request, self.params) 
  
        friends_id_list = []

        for friend in response_json['response']['items']:
            if (friend.get('deactivated') == 'deleted') or (friend.get('deactivated') == 'banned') or ((friend.get('is_closed') == '1') and (friend.get('can_access_closed') == '0')):
                pass
            else:
                friends_id_list.append(friend['id'])

        return friends_id_list

class Group:
    def get_info_about_group(self, group_id):
        self.params = {
                'access_token': access_token,
                'v': version,
                'group_id': group_id,
                'fields': 'members_count'
            }

        self.request = 'https://api.vk.com/method/groups.getById'

        group_dict = {}

        try:
            response_json = get_response_json(self.request, self.params)  
            time.sleep(0.3)
        except KeyError: 
            pass
        else:
            for group in response_json['response']:
                group_dict = {
                        'name': group['name'],
                        'gid': group['id'],
                        'members_count': group['members_count']
                    }
        finally:
            return group_dict

#-----------------------------------------------------------------------------------    

def get_response_json(request, params):
    response = requests.get(request, params) 
    response_json = response.json()
    return response_json

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
        response_json = get_response_json(request, params)
           
        for value in response_json['response']:
            user_id = value['id']
        return user_id  

def writing_groups_in_json(groups, path):
    group_list = []

    for group_id in groups:
        group_info = group.get_info_about_group(group_id)        
        group_list.append(group_info)
    
    with open(path , 'w', encoding='utf-8') as json_file:
        json.dump(group_list, json_file, ensure_ascii=False)

if __name__ == "__main__":
    #тестовый пользователь: 'eshmargunov' или '171691064'
    user_name = input('Введите имя или id пользователя: ')
    user_id = get_user_id(user_name)

    user = User()
    user_groups_id_list = user.get_groups_id_list(user_id)
    user_friends_id_list = user.get_friends_id_list(user_id)

    friends_groups_id_list = []

    for friend_id in user_friends_id_list:
        try:
            friend_groups_id_list = user.get_groups_id_list(friend_id)
            time.sleep(0.3)
        except KeyError:
            time.sleep(1)
        else:
            print('-' * 50)
            friends_groups_id_list.append(friend_groups_id_list)
        
    friends_groups_id_set = set()

    for group_list in friends_groups_id_list:
        for group_id in group_list:
            friends_groups_id_set.add(group_id)

    user_groups_id_set = set(user_groups_id_list)

    difference_groups = user_groups_id_set.difference(friends_groups_id_set)

    group = Group()

    writing_groups_in_json(difference_groups, 'groups.json')