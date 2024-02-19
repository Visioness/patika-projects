# # # # ------ INDEXING AND SLICING ------ # # # #
list = ['Python', True, 9, '3', 8.4, 'Hi-Kod', 'False', 4.7]

print(
    f'list[3] = {list[3]}\n'\
    f'list[5] = {list[5]}\n'\
    f'list[-1] = {list[-1]}\n'\
    f'list[2:6] = {list[2:6]}\n'\
    f'list[4:] = {list[3:]}\n'
)


# # # # ------ FILTERING STRINGS ------ # # # #
new_list = [element for element in list if type(element) == str]
print(f'New list that has only strings: {new_list}\n')


# # # # ------ ENUMERATING FRUITS ------ # # # #
fruits = ['Apple', 'Banana', 'Orange', 'Watermelon', 'Grape', 'Peach', 'Apricot']

for index, fruit in enumerate(fruits):
    print(f'Fruit in the {index}. index is: {fruit}')
