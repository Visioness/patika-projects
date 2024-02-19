# # # # ------ EXAM SCORES DICTIONARY ------ # # # #
import random

def get_scores():
    return random.randint(10, 100)

students = ['Ali', 'Veli', 'Ayşe', 'Fatma', 'Hayriye']
exams = {student: {
                'Math': get_scores(),
                'Physics':  get_scores(),
                'Chemistry': get_scores(),
            } for student in students}

name = input('Enter the student name: ')
course = input('Enter the course name: ')

print(f'{name} got {exams[name][course]} from {course}.\n\n')


# # # # ------ DICTIONARY MANIPULATION ------ # # # #
hi_kod = {
    course: {
        f'Week-{index}': [
            f'Assignment-{index * 2}',
            f'Assignment-{index * 2 + 1}',
        ]
        for index in range(10)
    }
    for course in ['Data-Science', 'Front-End', 'Mobile']
}

print(f'hi-kod dictionary: {hi_kod}\n')
print(f'hi_kod["Data-Science"]: {hi_kod["Data-Science"]}\n')

hi_kod['Data-Science']['Week-0'] = 'Just A String!'
hi_kod['New-Course'] = {'Week-0': ['Assignment-0']}

print(f'hi-kod dictionary: {hi_kod}\n')
print(f'hi_kod["Data-Science"]: {hi_kod["Data-Science"]}\n')
print(f'hi_kod["Data-Science"]["Week-0"]: {hi_kod["Data-Science"]["Week-0"]}\n')
print(f'hi_kod["New-Course"]: {hi_kod["New-Course"]}\n')

course = input('Enter the course you want to reach: ')
week = input('Enter the week as a number: ')
print(f'{course} assignments from Week-{week} are: {hi_kod[course][f"Week-{week}"]}')
