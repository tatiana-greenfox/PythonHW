from pprint import pprint

import requests

API_ID = '7309299'
access_token = '5f43c35946c516a3f879b50719786fa492274747a73658133de8cf7f0f1ee0f7d351fbb9bc742444bb763'
version = '5.103'

class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def get_user_name(self):
        if self.user_name.isdigit() == True:
            self.user_id = self.user_name
            return self.user_id
        else:
            self.screen_name = self.user_name
            return self.screen_name
      
    def get_user_url(self):
        self.user_url = 'vk.com/' + self.get_user_name()
        return self.user_url
    
    def get_user_id(self):
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

    def get_friends_list(self):            
        self.params = {
            'access_token': access_token,
            'v': version,
            'user_id': self.get_user_id(),
            'order': 'hints', 
            'count': '5000' 
            }

        response = requests.get('https://api.vk.com/method/friends.get' , self.params)
        pprint(response.text)
        # return friends_list

    def get_mutual_friends(self, user2_name):
        self.params = {
            'access_token': access_token,
            'v': version,
            'source_uid': self.get_user_id(),
            'target_uid': user2_name
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual' , self.params)
        pprint(response.text)


if __name__ == "__main__":
    user1 = User('alisa.aralova')
    user2 = User('alexeymechetnyi')

    # user1.get_mutual_friends(user2.get_user_id())

    # print(user1)


    user2.get_friends_list()
