def print_info(text_news , type_file):
  text_news = text_news.casefold()
  description_list = text_news.split()
  description_set = set(description_list)
  new_description_list = []

  for value in description_set:
      count_value = description_list.count(value)
      if len(value) >= 6:
          value_list = [value , count_value]
          new_description_list.append(value_list)
  sorted_list = sorted(new_description_list , key=lambda term: term[1])     
  slice_list = sorted_list[-1:-11:-1] 

  print(f"Топ 10 слов для {type_file}:")
  for value in slice_list:
    print(value[0] , '-' , value[1])
  print()

def get_json():
  import json

  with open('newsafr.json' , encoding = 'utf-8') as json_file:
    newsafr = json.load(json_file)
    items_list = newsafr['rss']['channel']['items']
    description = str()

    for value in items_list:
      description += value['description']

    print_info(description , 'json')