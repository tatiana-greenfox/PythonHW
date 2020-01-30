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

def get_xml():
  import xml.etree.ElementTree as xml_file

  tree = xml_file.parse('newsafr.xml')
  root = tree.getroot()
  description_text = str()

  for description in root.findall('channel/item/description'):
    description_text += description.text

  print_info(description_text , 'xml')

def get_json():
  import json

  with open('newsafr.json' , encoding = 'utf-8') as json_file:
    newsafr = json.load(json_file)
    items_list = newsafr['rss']['channel']['items']
    description = str()

    for value in items_list:
      description += value['description']

    print_info(description , 'json')

def main():
  info = '''Для получения топ 10 слов введите:
  - "1" для json-файла;
  - "2" для xml-файла введите;
  - "0" для выхода из программы
  '''

  print(info)
  
  while True:
    instraction = input('Введите номер иструкции: ')

    if instraction == '1':
      get_json()
    elif instraction == '2':
      get_xml()
    elif instraction == '0':
      print('Произведен выход из программы!')
      break

main()