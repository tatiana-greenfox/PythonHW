
class Contact:

    def __init__(self, name, surname, phone_number, status = False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.status = status
        self.additional_numbers = args
        self.additional_info = kwargs

    def __str__(self):

        if self.status == False or self.status == 0:
            self.status = 'нет'
        elif self.status == True or self.status == 1:
            self.status = 'да'

        user_info = f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_number}\nВ избранных: {self.status}'

        if self.additional_numbers and not self.additional_info:
            user_info += f'\nДополнительная информация\n\tДополнительные номера: '

            for tel_number in self.additional_numbers:
                user_info += f'{tel_number} '

        elif self.additional_info and not self.additional_numbers:
            user_info += '\nДополнительная информация\n'

            for type_info, info in self.additional_info.items():
                user_info += f'\t{type_info}: {info}\n'

        elif self.additional_numbers and self.additional_info:
            user_info += f'\nДополнительная информация\n\tДополнительные номера: '

            for tel_number in self.additional_numbers:
                user_info += f'{tel_number} '
            
            user_info += '\n'

            for type_info, info in self.additional_info.items():
                user_info += f'\t{type_info}: {info}\n'

        return user_info

class PhoneBook:

    def __init__(self, name_phonebook):
        self.name = name_phonebook
        self.contacts_list = []

    def print_contacts(self):

        if len(self.contacts_list) != 0:
            print(f'Список контактов из телефонной книги {self.name}:\n')
            for i, contact in enumerate(self.contacts_list):
                print(f'Контакт {i+1}\n{contact}\n')
        else:
            print(f'Телефонная книга {self.name} пустая!')

    def add_new_contact(self):

        name = input('Введите имя контакта: ')
        surname = input('Введите фамилию контакта: ')
        phone_number = input('Введите номер телефона контакта: ')
        question = input('Нажмите "+", если хотите ввести доп.информацию: ')

        if question == '+':
            status = input('Является ли контакт избранным Да/Нет: ')
            telephone_numbers = input('Введите через запятую доп. телефонные номера: ')
            dict_ = input('Введите прочие данные: ')

            if status == 'да':
                status = True
            elif status == 'нет':
                status = False

            if status and not telephone_numbers and not dict_:
                contact = Contact(name, surname, phone_number, status)
                self.contacts_list.append(contact)
    
            elif (status and telephone_numbers) and not dict_:
                telephone_num_list = telephone_numbers.split(',')
                telephone_numbers_tuple = tuple(telephone_num_list)
                contact = Contact(name, surname, phone_number, status, telephone_numbers_tuple)
                self.contacts_list.append(contact)

        else:
            contact = Contact(name, surname, phone_number)
            self.contacts_list.append(contact)

    def delete_contact(self):
        phone_number = input('Введите номер, который хотите удалить: ')

        if len(self.contacts_list) != 0:
            
            for contact in self.contacts_list:
                if contact.phone_number == phone_number:
                    self.contacts_list.remove(contact)
                    print('Контакт успешно удален!')
                else:
                    print(f'Контакста с телефонным номером {phone_number} в телефонной книге нет')
        else:
            print(f'Номер удалит не удалось, т.к. телефонная книга {self.name} пуста!')

    def search_favorites_contacts(self):
        if len(self.contacts_list) != 0:
            
            for contact in self.contacts_list:
                if contact.status == True:
                    print(contact)
        else:
            print(f'Телефонная книга {self.name} пуста!')

    def search_contact(self):

        name = input('Введите имя контакта: ')
        surname = input('Введите фамилию контакта: ')

        if len(self.contacts_list) != 0:
            
            for contact in self.contacts_list:
                if (contact.name == name) and (contact.surname == surname):
                    print(contact)
        else:
            print(f'Телефонная книга {self.name} пуста!')

def create_telephone_book(name):

    phone_book = PhoneBook(name)

    return phone_book


if __name__ == "__main__":
    # Имя: Jhon
    # Фамилия: Smith
    # Телефон: +71234567809
    # В избранных: нет
    # Дополнительная информация:
    # 	 telegram : @jhony
    # 	 email : jhony@smith.com

    tatiana = Contact('Tatiana', 'Krylova', '8-925-***-**-**', '8-916-***-15-**', '3', email='1993greenfox@gmail.com', telegram='@test')

    print(tatiana)

    instruction = '''

        - Для создания нового контакта нажмите "a" или "1"
        - Для удаления контакта по номеру телефона нажмите "d" или "2"
        - Для поиска избранных контактов нажмите "f" или "3"
        - Для поиска контакта по имени и фамилии нажмите "s" или "4"
        - Для просмотра всех контактов телефонной книги нажмите "p" или "0"
        - Для выхода из приложения нажмите "e" или "*"
    
    '''

    phonebook_name = input('Введите название телефонной книги: ')
    phonebook = create_telephone_book(phonebook_name)

    while True:
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
        elif instruction == 'e' or instruction == '*':
            break