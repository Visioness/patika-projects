# # # # ------ 01 - INCOME TAX CALCULATION ------ # # # #
salary = abs(float(input('Entery your salary: ')))
if 45000 >= salary > 25000:
    new_salary = salary * 0.75
elif 25000 >= salary > 10000:
    new_salary = salary * 0.90
elif 10000 >= salary:
    new_salary = salary * 0.95
else:
    new_salary = salary * 0.70

print(f'Without Taxes: {salary}, With Taxes: {new_salary}\n\n')


# # # # ------ 02 - USER AUTHENTICATION CHECK ------ # # # #
username = input('Enter your username: ')
password = input('Enter your password: ')
if len(password) >= 6:
    print(f'Username: {username}, Password: {password}\n\n')
else:
    print('Invalid usage. Enter a password with at least 6 characters!\n\n')


# # # # ------ 03 - ACCOUNT CREATION VALIDATION ------ # # # #
username = input('Enter your username: ')
while True:
    password = input('Enter your password: ')
    if 10 > len(password) > 5:
        print('Your account has been created!')
        break
    else:
        print('Your password must be between 5 and 10 characters in length.')

print(f'Username: {username}, Password: {password}\n\n')


# # # # ------ 04 - LIMITED LOGIN ATTEMPTS ------ # # # #
password_in_data = 'thisissecret'

username = input('Enter your username: ')
reprompt = 3
while reprompt > 0:
    user_password = input('Enter your password: ')
    if user_password == password_in_data:
        print('Logged in!\n\n')
        break
    reprompt -= 1
    print(f'Wrong password. Remaining attempts: {reprompt}')
    if reprompt == 0:
        print('No attempts left. You are blocked!\n\n')
    