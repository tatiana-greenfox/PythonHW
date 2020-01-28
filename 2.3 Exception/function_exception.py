documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
  }

#Задача 1 

#Функция поиска владельца документа по номеру
def get_name_person(document_catalog):
  number_document = input('Введите номер документа: ')

  document_dict = {}
  result = 0  
  
  for document in document_catalog:  
    if document['number'] == number_document:
      document_dict = document
      result = 1

  if result == 0:
    print('Номер документа не найден!')
    get_name_person(document_catalog)
  else:
    print(f"По введенному вами документу найден: {document_dict['name']}")

#Функция вывода всех документа в виде списка   
def get_list_document(document_catalog):
  for document in document_catalog:
    document_list = []

    for value in document.values():
      document_list.append(value)
    print(f'{document_list[0]} "{document_list[1]}" "{document_list[2]}"')

#Функция поиска номера полки, на которой лежит документ по его номеру
def get_number_shelf(directori_catalog):
  number_document = input('Введите номер документа: ')
  number_shelf = 0
  result = 0 

  for key, values in directori_catalog.items():
    for number in values:
      if number == number_document:
        number_shelf = key
        result = 1

  if result == 0:
    print('Номер документа не найден!')
    get_number_shelf(directori_catalog)
  else:
    print(f"Документ {number_document} находится на полке номер {number_shelf}")

#Функция создания нового документа и добавления его данных в соответствующие каталоги 
def add_new_document(document_catalog , directori_catalog): 
  new_document_type = input('Введите тип документа: ')
  new_document_number = input('Введите номер документа: ')
  new_name = input('Введите имя владельца документа: ')
  number_shelf = input('Введите номер полки, на которой будет храниться документ: ')

  document_dict = {}
  result = 0

  print()

  #Добавление пользовательских данных в список документов
  for document in document_catalog:
    if new_document_number != document['number']:
      document_dict = document_dict.fromkeys(document)
      document_dict['type'] = new_document_type
      document_dict['number'] = new_document_number
      document_dict['name'] = new_name
  document_catalog.append(document_dict)

  #Добавление номера нового документа на введенную пользователем полку
  for key, value in directori_catalog.items():
      if key == number_shelf:
        value.append(new_document_number)
        result = 1    
  
  if result == 0:
    print('Документ не может быть сохранен, тк полки с таким номером в каталоге нет!')
  else:
    print('Введенные вами данные успешно сохранены! Документ добавлен в картотеку!\n')
    print(document_catalog , '\n')

    print(f"Документ c номером {new_document_number} успешно добавлен на полку {number_shelf}\n")
    print(directori_catalog)

#Задача 2 

#Функция удаления документа из базы 
def delete_document(document_catalog , directori_catalog):
  number_document = input('Введите номер документа: ')
  result = 0 

  #Удаление документа из каталога
  for document in document_catalog:
    if document['number'] == number_document:
      document.clear()
      document_catalog.remove(document)
      result = 1
   
  #Удаление номера документа из каталога с номерами полок
  number_shelf = 0

  for key, values in directori_catalog.items():
    for number in values:
      if number == number_document:
        values.remove(number)
        number_shelf = key
        result = 1

  if result == 0:
    print('Номер документа не найден!')
    delete_document(document_catalog , directori_catalog)
  else:
    print(f"Документ под номером {number_document} был успешно удален из каталога\n")
    print(document_catalog , '\n')

    print(f"Документ под номером {number_document} был успешно удален с полки {number_shelf}\n")
    print(directori_catalog)

#Функция создания новой полки
def add_new_shelf(directori_catalog, number_shelf):
  new_directori_catalog = {}

  for key in directori_catalog.keys():
    if key != number_shelf:
      new_directori_catalog = directori_catalog
  new_directori_catalog.setdefault(number_shelf)
  new_directori_catalog[number_shelf] = []
  print(f"Новая полка успешно добавлена в перечень {new_directori_catalog}")

#Функция перемещения документа с полки на полку
def move_document(directori_catalog):
  number_document = input('Введите номер документа: ')
  number_shelf_on = input('Введите номер полки: ')
  number_shelf_off = 0 
  result = 0

  for key, values in directori_catalog.items():
    for number in values:
      if number == number_document:
        values.remove(number)
        number_shelf_off = key 
        result = 1

  if result == 0:
    print('Номер документа не найден!')
  else:
    add_new_shelf(directori_catalog , number_shelf_on)
    directori_catalog[number_shelf_on].append(number_document)

    print(f"Документ под номером {number_document} был успешно перемещен с полки {number_shelf_off} на полку {number_shelf_on}\n")
    print(directori_catalog)

#функция получения всех имен владельцев документов из каталога
def get_all_names(document_catalog):
    for value in document_catalog:
        try:
            value['name']
        except KeyError as e:
            print(f"Ошибка! Не могу вывести значение, отсутствует ключ {e}")
        else:
            print(value['name'])
      
def main():
  info = '''
  --- Инструкция для работы с программой "Секретарь" ---

  - Для получения имени человека по номеру документа, введите "p" или "people";
  - Для получения информации по всем документам в виде списка, введите "l" или "list";
  - Для получения информации о местонахождении документа, введите "s" или "shelf";
  - Для создания нового документа и добавления его в картотеку, введите "a" или "add";
  - Для удаления документа из всей картотеки, введите "d" или "delete"; 
  - Для создания новой полки, введите "as"; 
  - Для перемещения документа с одной полки на другую, введите "m" или "move";
  - Для получения списка всех имен владельцев документов, введите "n" или "name";
  - Для выхода из программы, введите "e" или "exit".
  '''
  print(info)

  while True:
    instruction = input('Введите инструкцию: ')

    if (instruction == 'p') or (instruction == 'people'):
      get_name_person(documents)
      print()
    elif (instruction == 'l') or (instruction == 'list'):
      get_list_document(documents)
      print()
    elif (instruction == 's') or (instruction == 'shelf'):
      get_number_shelf(directories)
      print()
    elif (instruction == 'a') or (instruction == 'add'):
      add_new_document(documents, directories)
      print()
    elif (instruction == 'd') or (instruction == 'delete'):
      delete_document(documents, directories)
      print()
    elif (instruction == 'as'):
      add_new_shelf(directories , input('Введите номер полки: '))
      print()
    elif (instruction == 'm') or (instruction == 'move'):
      move_document(directories)
      print()
    elif (instruction == 'n') or (instruction == 'name'):
      get_all_names(documents)
      print()
    elif (instruction == 'e') or (instruction == 'exit'):
      print('Спасибо за использование нашей программы! До свидания!')
      break

main()