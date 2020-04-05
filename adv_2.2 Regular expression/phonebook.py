import csv
import re

def read_phonebook(path):
    with open(path, encoding='utf-8') as csv_file:
        line = csv.reader(csv_file, delimiter=",")
        contacts_list = list(line)

    return contacts_list

def split_fio(phonebook):

    contacts_list = read_phonebook(phonebook)

    for contact in contacts_list:
        lastname = re.split(r"\s", contact[0])
        name = re.split(r"\s", contact[1])
        surname = re.split(r"\s", contact[2])
        
        if len(lastname) == 3:
            contact[0] = lastname[0] #lastname
            contact[1] = lastname[1] #name
            contact[2] = lastname[2] #surname
        elif len(lastname) == 2:
            contact[0] = lastname[0] #lastname
            contact[1] = lastname[1] #name
        elif len(name) == 3:
            contact[0] = name[0] #lastname
            contact[1] = name[1] #name
            contact[2] = name[2] #surname
        elif len(name) == 2:
            contact[1] = name[0] #name
            contact[2] = name[1] #surname
        elif len(surname) == 3:
            contact[0] = surname[0] #lastname
            contact[1] = surname[1] #name
            contact[2] = surname[2] #surname
        elif len(surname) == 2:
            contact[1] = surname[0] #name
            contact[2] = surname[1] #surname
    return contacts_list
                
def replace_telephone_number(phonebook):

    contacts_list = merge_contacts(phonebook)

    pattern_phonenumber = re.compile(r"(\+7|8)\s*\(?(495)[\)\-]?\s*(\d{3})\-?(\d{2})\-?(\d{2})\s*(\(?доб\.\s*(\d*)\)?)?")
    
    for contact in contacts_list:
        phone_number = contact[5]

        if phone_number and ('доб' not in phone_number):
            contact[5] = pattern_phonenumber.sub(r"+7(495)\3-\4-\5", phone_number)
        elif phone_number and ('доб' in phone_number):
            contact[5] = pattern_phonenumber.sub(r"+7(495)\3-\4-\5 доб.\7", phone_number)
    
    return contacts_list

def merge_contacts(phonebook):

    contacts_list = split_fio(phonebook)

    for contact_1 in contacts_list:
        for contact_2 in contacts_list:

            if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1]:
                if contact_2[2]:
                    contact_1[2] = contact_2[2]

                if contact_2[3]:
                    contact_1[3] = contact_2[3]

                if contact_2[4]:
                    contact_1[4] = contact_2[4]

                if contact_2[5]:
                    contact_1[5] = contact_2[5]

                if contact_2[6]:
                    contact_1[6] = contact_2[6]

    for contact in contacts_list:
        count = contacts_list.count(contact)

        if count > 1:
            contacts_list.remove(contact)     

    return contacts_list     
                         
def save_changes(phonebook):
    contacts_list = replace_telephone_number(phonebook)

    with open('new_phonebook.csv', 'w', encoding='utf-8') as new_file:
        new_phonebook = csv.writer(new_file)
        new_phonebook.writerows(contacts_list)


if __name__ == "__main__":
    save_changes('phonebook_raw.csv')