from class_contact import Contact

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
                telephone_numbers_list = telephone_numbers.split(',')
                telephone_numbers_tuple = tuple(telephone_numbers_list)
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

if __name__ == "__main__":
    phonebook = PhoneBook('Phonebook_1')