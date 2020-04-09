import string
import random


print('Welcome to HNG Tech')
def get_details():
    firstName = input('Enter your First Name: ')
    lastName = input('Enter your Last Name: ')
    email = input('Enter your Email Address : ')

    details = [firstName,lastName,email]

    return details

def gen_password(details):
    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters) for i in range(length))
    password = str(details[0][0:2] + details[1][-2:] + random_password)
    return password

status = True
container = []

while status:
    details = get_details()
    password = gen_password(details)
    print("Your password is: " + str(password))

    password_loop = True
    while password_loop:
        password_like = input(str("Are you satisfied with the generated password? If YES, Enter Y,for No,Enter N and supply your preferred password: ")).lower()
        if password_like == "y":
            details.append(password)
            password_loop = False
        elif password_like == 'n':
            pass_len = True
            while pass_len:
                user_password = input(str("Enter password longer than or equal to 7 characters: ")).lower()
                if len(user_password) >= 7:
                    details.append(user_password)

                    pass_len = False
                    password_loop = False
                else:
                    print("Your Password is less than 7 Characters")
                    user_password = input(str("Enter password longer than or equal to 7 characters: "))
        else:
            continue
    container.append(details)
    new_user = input(str("Would you like to enter a new user? Yes or No: ")).lower()
    if new_user == "no":

        status = False
        for i in range(len(container)):
            print(f'firstname:{container[i][0]}, lastname: {container[i][1]}, email: {container[i][2]},password: {container[i][3]}')
    else:
        status = True

