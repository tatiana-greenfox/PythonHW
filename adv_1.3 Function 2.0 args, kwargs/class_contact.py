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

            for number in self.additional_numbers:
                user_info += f'{number} '

        elif self.additional_info and not self.additional_numbers:
            user_info += '\nДополнительная информация\n'

            for type_info, info in self.additional_info.items():
                user_info += f'\t{type_info}: {info}\n'

        elif self.additional_numbers and self.additional_info:
            user_info += f'\nДополнительная информация\n\tДополнительные номера: '

            for number in self.additional_numbers:
                user_info += f'{number} '
            
            user_info += '\n'

            for type_info, info in self.additional_info.items():
                user_info += f'\t{type_info}: {info}\n'

        return user_info

if __name__ == "__main__":
    # Имя: Jhon
    # Фамилия: Smith
    # Телефон: +71234567809
    # В избранных: нет
    # Дополнительная информация:
    # 	 telegram : @jhony
    # 	 email : jhony@smith.com

    tatiana = Contact('Tatiana', 'Krylova', '8-925-***-**-**', True, '8-916-***-15-**', '+7(495)7770045', email='1993greenfox@gmail.com', telegram='@test')

    print(tatiana)