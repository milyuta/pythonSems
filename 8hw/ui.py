def get_action():
    mode = int(input("input your action: "\
        "1 - find user to id\n\
         2 - find user to surname\n\
         3 - add new user\n\
         4 - delete information\n\
         5 - edit user information"))
    return mode



def get_info_3 ():
    info = []
    description = input('input id ')
    info.append(description)
    last_name = input('input last name: ')
    info.append(last_name)
    first_name = input('input name: ')
    info.append(first_name)
    second_name = input('input second name: ')
    info.append(second_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('input phone number: ')
            if len(phone_number) != 11:
                print('phone number must have 11 nums, retry ')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('phone number must consist of nums, retry ')
    info.append(phone_number)
    
    return info


def get_info_1():
    id =int(input('input the user`s id:'))

def get_info_2():
    id =input('input the user`s last name:')