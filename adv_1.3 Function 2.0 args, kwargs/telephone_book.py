from class_phonebook import PhoneBook

def create_phonebook(name):
    phonebook = PhoneBook(name)
    return phonebook

def select_phonebook(name):
    phonebooks_list = []
   
    if len(phonebooks_list) != 0:

        for phonebook in phonebooks_list:
            if phonebook.name == name:
                print(f'Книга с таким именем уже существует')
                return phonebook
            else:
                phonebook_new = create_phonebook(name)
                phonebooks_list.append(phonebook_new)
                print(f'Телефонная книга {name} успешно создана')
                return phonebook_new
                
    else:
        phonebook_new = create_phonebook(name)
        phonebooks_list.append(phonebook_new)
        return phonebook_new

def save_phonebook(phonebooks_list):
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
            phonebook.search_contact()
        elif instruction == 'p' or instruction == '0':
            phonebook.print_contacts()
        elif instruction == 'e':
            break

if __name__ == "__main__":

    phonebook_name = input('Введите название телефонной книги: ')

    phonebook = select_phonebook(phonebook_name)

    with open('help.txt', encoding='utf-8') as help_file:
        print(f'\n{help_file.read()}\n')
    
    run_phonebook()