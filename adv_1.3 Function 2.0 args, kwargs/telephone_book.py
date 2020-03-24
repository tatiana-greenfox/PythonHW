from class_phonebook import PhoneBook

def create_phonebook(name):
    phonebook = PhoneBook(name)
    return phonebook

def select_phonebook(name):
    phonebooks_list = []
   
    if len(phonebooks_list) != 0:

        for phonebook in phonebooks_list:
            if phonebook.name != name:
                phonebook_new = create_phonebook(name)
                phonebooks_list.append(phonebook_new)
                print(f'Телефонная книга {name} успешно создана')
                return phonebook_new
            else:
                print(f'Книга с таким именем уже существует')
                return phonebook
    else:
        phonebook_new = PhoneBook(name)
        phonebooks_list.append(phonebook_new)
        return phonebook_new

def save_phonebooks(phonebooks_list):
    pass

def run_phonebook():
    
    while True:
        instruction = input('Введите инструкцию: ')

        if instruction == 'a' or instruction == '1':
            phonebook.add_new_contact()
        elif instruction == 'd' or instruction == '2':
            phonebook.delete_contact()
        elif instruction == 'f' or instruction == '3':
            phonebook.search_favorites_contacts()
        elif instruction == 's' or instruction == '4':
            phonebook.search_contact
        elif instruction == 'p' or instruction == '0':
            phonebook.print_contacts()
        elif instruction == 'et' or instruction == '*':
            print('Вы вышли из телефонной книги.\n Для выбора другой нажмите на "t", а для выхода их приложения "e"')
        # elif instruction == 't':
        #     phonebook_name = input('Введите название телефонной книги: ')
        #     phonebook = select_phonebook(phonebook_name)
        elif instruction == 'e':
            break

if __name__ == "__main__":

    instruction_info = '''

        - Для создания нового контакта нажмите "a" или "1"
        - Для удаления контакта по номеру телефона нажмите "d" или "2"
        - Для поиска избранных контактов нажмите "f" или "3"
        - Для поиска контакта по имени и фамилии нажмите "s" или "4"
        - Для просмотра всех контактов телефонной книги нажмите "p" или "0"
        - Для выхода из телефонной книги нажмите и выбора  "et" 
        - Для выхода из приложения нажмите "e" или "*"
    
    '''

    phonebook_name = input('Введите название телефонной книги: ')

    phonebook = select_phonebook(phonebook_name)

    print(instruction_info)
    
    run_phonebook()