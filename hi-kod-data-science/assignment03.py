# # # # ------ CALCULATE CIRCLE AREA ------ # # # #
def calculate_area():
    pi = float(input('Enter the pi value: '))
    radius = float(input('Enter the radius of the circle: '))

    area = pi * (radius ** 2)
    print(f'Area of the circle is: {area:.2f}')


# # # # ------ CALCULATE FACTORIAL ------ # # # #
def factorial(number):
    if number >= 0:
        result = 1
        if number >= 2:
            for n in range(2, (number + 1)):
                result *= n
        print(f'{number}! is: {result}')
    else:
        print('Factorials are undefined for negative integers!')


# # # # ------ CALCULATE AGE ------ # # # #
def calculate_age(year_of_birth):
    return 2024 - year_of_birth


# # # # ------ CHECK RETIREMENT STATUS ------ # # # #
def is_retired(year_of_birth, name):
    age = calculate_age(year_of_birth)
    if age >= 65:
        print(f'Congratulations, {name}! You have reached retirement age.')
    else:
        print(f'{name}, you have {65 - age} years left until retirement.')


calculate_area()
factorial(5)
factorial(7)
factorial(0)
print(calculate_age(1999))
is_retired(1959, 'Aygun')
is_retired(1999, 'Aygun')
