# # # # ------ 01 CONVERTING DATA TYPES ------ # # # #
age, percent, points = '24', 12.3, 10
print(f'Age: {type(age)}, Percent: {type(percent)}, Points: {type(points)}')

age = int(age)
percent = str(percent)
points = float(points)
print(f'Age: {type(age)}, Percent: {type(percent)}, Points: {type(points)}\n\n')


# # # # ------ 02 COMPARISON AND LOGICAL OPERATORS ------ # # # #
age_01, age_02, age_03 = 32, 24, 62
print(f'age_01 > age_02: {age_01 > age_02}\n' 
    f'age_02 == age_03: {age_02 == age_03}\n'
    f'(age_03 >= age_01 and age_03 < age_02) or age_02 != age_01: {(age_03 >= age_01 and age_03 < age_02) or age_02 != age_01}\n'
    f'not(age_03 > age_01 > age_02): {not(age_03 > age_01 > age_02)}\n\n')


# # # # ------ 03 BASIC ARITHMETIC OPERATIONS ------ # # # #
# We can also round the result to reduce precision errors
x = float(input('Enter "x" value: '))
y = float(input('Enter "y" value: '))
 
addition = round(x + y, 2)
subtraction = round(x - y, 2)
multiplication = round(x * y, 2)
division = round(x / y, 2)
print(f'Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}\n\n')


# # # # ------ 04 GETTING USER INFORMATION ------ # # # #
user_name, age, city, job = input('Enter your information in the following format: \nUsername,Age,City,Job\n').split(',')
print(f'Username: {user_name}\n'
      f'Age: {age}\n'
	  f'City: {city}\n'
      f'Job: {job}\n\n')


# # # # ------ 05 - STRING METHODS ------ # # # #
workshop = 'Hi-Kod Veri Bilimi Atölyesi'

words = workshop.split() # Splitted
uppercased_workshop = workshop.upper() # Uppercased
lowercased_workshop = workshop.lower() # Lowercased

print(f'Splitted: {words}\n'
      f'Uppercased: {uppercased_workshop}\n'
	  f'Lowercased: {lowercased_workshop}\n\n')


# # # # ------ 06 - EVEN | ODD NUMBERS ------ # # # #
even_numbers, odd_numbers = '', ''
numbers = '0123456789'
for char in numbers:
	if int(char) % 2 == 0:
		even_numbers += char
	else:
		odd_numbers += char

print(f'Numbers: {numbers}, Even Numbers: {even_numbers}, Odd Numbers: {odd_numbers}\n\n')