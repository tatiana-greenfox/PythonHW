import json
import requests

class MyIterator:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf-8')
        self.countries_list = json.load(self.file)
        self.countrie_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        countrie = self.countries_list[self.countrie_index]
        self.countrie_index += 1
        
        if self.countrie_index == len(self.countries_list):
            raise StopIteration
        countrie_official_name = countrie['name']['official']
        countrie_common_name = countrie['name']['common']
        url = f'https://en.wikipedia.org/wiki/{countrie_common_name}'

        if requests.get(url).status_code == 404:
            return {countrie_official_name: 'Wikipedia article not found'}
        else:
            return {countrie_official_name: url}
            
                
if __name__ == "__main__":
    countries = []
    countries_obj = MyIterator('countries.json')

    for i, countrie in enumerate(countries_obj):
        countries.append(countrie)
        print(f'Обранодано {i+1} стран. Осталось {len(countries_obj.countries_list) - (i+1)}')

    with open('response_wiki.json', 'w') as response_json:
        json.dump(countries, response_json)
    print('Запись успешно завершена!')