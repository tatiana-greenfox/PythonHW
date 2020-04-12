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
        fio_str = ' '.join(contact[:3])
        fio_list = re.findall(r'\w+', fio_str)
        
        if len(fio_list) == 3:
            contact[0] = fio_list[0] 
            contact[1] = fio_list[1] 
            contact[2] = fio_list[2] 
        elif len(fio_list) == 2:
            contact[0] = fio_list[0] 
            contact[1] = fio_list[1] 
        else:
            contact[0] = fio_list[0]

    return contacts_list
                
def replace_telephone_number(phonebook):

    contacts_list = merge_contacts(phonebook)

    pattern_phonenumber = re.compile(r"(\+7|8)\s*\(?(495)[\)\-]?\s*(\d{3})\-?(\d{2})\-?(\d{2})\s*(\(?доб\.\s*(\d*)\)?)?")
    
    for contact in contacts_list:
        phone_number = contact[5]

        if phone_number:
            if 'доб' not in phone_number:
                contact[5] = pattern_phonenumber.sub(r"+7(495)\3-\4-\5", phone_number)
            else:
                contact[5] = pattern_phonenumber.sub(r"+7(495)\3-\4-\5 доб.\7", phone_number)
    
    return contacts_list

def merge_contacts(phonebook):

    contacts_list = split_fio(phonebook)
   
    for contact_1 in contacts_list:
        for contact_2 in contacts_list:

            if contact_1[0] == contact_2[0] and contact_1[1] == contact_2[1]:
                index = 2

                if  contact_2[index]:
                    while 2 <= index <= 6:
                        contact_1[index] = contact_2[index]
                        index += 1

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