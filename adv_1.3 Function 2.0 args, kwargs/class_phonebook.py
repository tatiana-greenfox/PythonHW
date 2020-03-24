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

        instruction = input('Eсли хотите ввести доп.информацию, нажмите "+", усли нет "-": ')

        if instruction == '+':
            status = input('Является ли контакт избранным Да/Нет: ')

            if status == 'да' or status == 'yes' or status == '1':
                status = True
            elif status == 'нет' or status == 'no' or status == '0':
                status = False
            else:
                status = False

            telephone_numbers = input('Доп. номера для связи: ')
            other_info = input('Социальные сети: ')

            other_info_list = other_info.split(', ')
            other_info_list_new = []

            for info_str in other_info_list:
                other_info_list_new.append(info_str.split(': '))

            informations_dict = dict(other_info_list_new)

            telephone_numbers_list = telephone_numbers.split(', ')
            telephone_numbers_tuple = tuple(telephone_numbers_list)

            contact = Contact(name, surname, phone_number)

            contact.status = status
            contact.additional_numbers = telephone_numbers_tuple
            contact.additional_info = informations_dict

            self.contacts_list.append(contact)

            print('\n----------------------------------------\n')
            print(f'Контакт {name} {surname} успешно добавлен!\n')

        else:
            contact = Contact(name, surname, phone_number)

            self.contacts_list.append(contact)

            print('\n----------------------------------------\n')
            print(f'Контакт {name} {surname} успешно добавлен!')

        return self.contacts_list

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
    phonebook.add_new_contact()
    phonebook.print_contacts()