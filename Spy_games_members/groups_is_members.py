import requests
import time
import json

access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

class User:
    def get_id(self, user_name):
        if type(user_name) == str:
            if user_name.isdigit() == True:
                self.user_id = user_name
                return self.user_id
            else:
                self.screen_name = user_name

                self.params = {
                    'access_token': access_token,
                    'v': version,
                    'user_ids': self.screen_name
                }

                self.request = 'https://api.vk.com/method/users.get'
                response_json = get_response_json(self.request, self.params)
                
                for value in response_json['response']:
                    self.user_id = value['id']
                return self.user_id  
        elif type(user_name) == int:
            self.user_id = user_name
            return self.user_id

    def get_groups_list(self, user_name):
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': self.get_id(user_name),
            'extended': '1',
            'count': '1000'
        }

        self.request = 'https://api.vk.com/method/groups.get'

        response_json = get_response_json(self.request, self.params)
        items_list = response_json['response']['items']

        return items_list

    def get_groups_id_list(self, user_name):
        groups_list = self.get_groups_list(user_name)
        groups_id_list = []

        for group in groups_list:
            groups_id_list.append(group['id'])
        
        return groups_id_list    

    def get_friends_list(self, user_name):            
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': self.get_id(user_name),
            'order': 'hints', 
            'fields': 'deactivated'
            }

        self.request = 'https://api.vk.com/method/friends.get'

        response_json = get_response_json(self.request, self.params) 

        return response_json['response']['items'] 

    def get_friends_id_list(self, user_name):            
        friends_list = self.get_friends_list(user_name)
  
        friends_id_list = []

        for friend in friends_list:
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

        response_json = get_response_json(self.request, self.params)  
        time.sleep(0.35)

        for group in response_json['response']:
            group_dict = {
                    'name': group['name'],
                    'gid': group['id'],
                    'members_count': group['members_count']
                }

        return group_dict


#-----------------------------------------------------------------------------------    

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
    # user_name = 'eshmargunov'

    user = User()

    user_groups_id_list = user.get_groups_id_list(user_name)
    user_friends_id_list = user.get_friends_id_list(user_name)

    groups_list = []

    request = 'https://api.vk.com/method/groups.isMember'

    for group_id in user_groups_id_list:
        member_status_list = []
        groups_dict = {}

        for friend_id in user_friends_id_list:
            params = {
                    'access_token': access_token,
                    'v': version,
                    'group_id': group_id,
                    'user_ids': friend_id,
                    'extended': 1
                }

            response_json = get_response_json(request, params)
            time.sleep(0.35)

            for value in response_json['response']:
                member_status_list.append(value['member'])

        groups_dict = {group_id:  member_status_list}
        groups_list.append(groups_dict)

    difference_groups_set = set()
    intersection_groups_set = set()

    count_friends = 10 #кол-во друзей в группе

    for group_dict in groups_list:
        for key, value in group_dict.items():
            if 1 in value:
                if value.count(1) < count_friends:
                    intersection_groups_set.add(key)
            else:
                difference_groups_set.add(key)

    group = Group()

    writing_groups_in_json(difference_groups_set, 'difference_groups.json')
    writing_groups_in_json(intersection_groups_set, 'intersection_groups.json')