from modules.config import ACCESS_TOKEN, VERSION
from modules.common_functions import get_response_json
from modules.class_user import User
from modules.class_group import Group

import time
import json

# Функция получения общего списка id групп для всех друзей пользователя.

def get_friends_groups_id_list(friends_id_list):
    friends_groups_id_list = []

    for friend_id in friends_id_list:
        try:
            friend = User(friend_id)
            friend_groups_id_list = friend.get_groups_id_list() # получение списка id групп для одного друга 
            friends_groups_id_list.extend(friend_groups_id_list) # запись полученного списка в общий список
            time.sleep(0.35)
        except KeyError:
            time.sleep(1)

    return friends_groups_id_list

# Функция осуществляющая проверку, что в группе встречается не более чем N друзей пользователя.

def checking_count_friends_in_group(groups_set, friends_groups_id_list, count_friends):

    for group_id in groups_set:

        # Если id группы встретился более 10 раз в списке id групп всех друзей пользователя, удаляем его из множества.
        if friends_groups_id_list.count(group_id) > count_friends:
            groups_set.discard(group_id)

    return groups_set

# Функция для записи групп в json-файл.

def writing_groups_in_json(groups, path):
    groups_list = []

    for group_id in groups:
        group = Group(group_id)
        group_info = group.get_info_about_group()        
        groups_list.append(group_info)
    
    with open(path , 'w', encoding='utf-8') as json_file:
        json.dump(groups_list, json_file, ensure_ascii=False)

# Функция получения множеств групп для заданного пользователя.

def get_groups_sets_for_user(user):
    user_groups_id_list = user.get_groups_id_list()
    user_friends_id_list = user.get_friends_id_list()

    friends_groups_id_list = get_friends_groups_id_list(user_friends_id_list)

    user_groups_id_set = set(user_groups_id_list)
    friends_groups_id_set = set(friends_groups_id_list)

    # Поиск групп, в которых состоит только текущий пользователь и запись их в файл.
    difference_groups = user_groups_id_set.difference(friends_groups_id_set)
    writing_groups_in_json(difference_groups, 'difference_groups.json')
    
    # Поиск групп, в которых состоит неболее чем N друзей пользователя и запись их в файл.
    intersection_groups = user_groups_id_set.intersection(friends_groups_id_set)
    intersection_groups_new = checking_count_friends_in_group(intersection_groups, friends_groups_id_list, 10)
    writing_groups_in_json(intersection_groups_new, 'intersection_groups.json')

if __name__ == "__main__":
    # Данные пользователя: eshmargunov / 171691064
    user_name = input('Введите имя пользователя: ')

    user = User(user_name)

    get_groups_sets_for_user(user)