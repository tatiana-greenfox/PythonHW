def print_info(text_news):
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
  print(text_news , '\n\nТоп 10 слов:')
  
  for value in slice_list:
    print(value[0] , '-' , value[1])
  print()

def get_xml():
  import xml.etree.ElementTree as xml_file

  tree = xml_file.parse('newsafr.xml')
  root = tree.getroot()

  for description in root.findall('channel/item/description'):
    description_text = description.text
    print_info(description_text)

def get_json():
  import json

  with open('newsafr.json' , encoding = 'utf-8') as json_file:
    newsafr = json.load(json_file)
    items_list = newsafr['rss']['channel']['items']

    for value in items_list:
      description = value['description']
      print_info(description)

def main():
  print('Для получения информации введите xml или json, выхода exit')
  while True:
    instraction = input('Введите тип файла: ')

    if instraction == 'xml':
      print('Информация по xml-файлу\n\n')
      get_xml()
    elif instraction == 'json':
      print('Информация по json-файлу\n\n')
      get_json()
    elif instraction == 'exit':
      print('Произведен выход из программы!')
      break

main() 