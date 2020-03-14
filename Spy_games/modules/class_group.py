from modules.config import ACCESS_TOKEN, VERSION
from modules.common_functions import get_response_json

import time

class Group:

    def __init__(self, group_id):
        self.group_id = group_id

    # Функция получения списка участников группы.

    def get_members_group(self):
        offset = 0

        params = {
            'access_token': ACCESS_TOKEN,
            'v': VERSION,
            'group_id': self.group_id,
            'offset': offset,
            'count': 1000
        }

        request = 'https://api.vk.com/method/groups.getMembers'

        response_json = get_response_json(request, params) 
        members_list = response_json['response']['items']

        while len(members_list) < response_json['response']['count']:
            offset += 1000
            params = {
                'access_token': ACCESS_TOKEN,
                'v': VERSION,
                'group_id': self.group_id,
                'offset': offset,
                'count': 1000
            }

            response_json = get_response_json(request, params) 
            time.sleep(0.35)

            members_list.extend(response_json['response']['items'])

        return members_list

    # Функция получения информации о группе по её id.

    def get_info_about_group(self):
        params = {
            'access_token': ACCESS_TOKEN,
            'v': VERSION,
            'group_id': self.group_id,
            'fields': 'members_count'
        }

        request = 'https://api.vk.com/method/groups.getById'

        group_dict = {}
        
        response_json = get_response_json(request, params)  
        time.sleep(0.35)
        
        for group in response_json['response']:
            group_dict = {
                    'name': group['name'],
                    'gid': group['id'],
                    'members_count': group['members_count']
                }

        return group_dict

if __name__ == "__main__":
    group = Group(8564)
    print(group.get_members_group())  