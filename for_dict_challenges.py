# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
from collections import Counter
list_student = []
for student in students:
    list_student.append(student['first_name'])
count = Counter(list_student)
for student in set(list_student):
    print(f'{student}: {count[student]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('\n\n')
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

list_student = []
for student in students:
    list_student.append(student['first_name'])
count = Counter(list_student).most_common(1)
print(f'Самое частое имя среди учеников: {count[0][0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша
print('\n\n')
# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
class_number = 0
for school_class in school_students:
    list_student = []
    class_number += 1
    for student in school_class:
        list_student.append(student['first_name'])
    count = Counter(list_student).most_common(1)
    print(f'Самое частое имя в классе {class_number} : {count[0][0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('\n\n')
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_number in school:
    count_boys = 0
    count_girls = 0
    for student in class_number['students']:
        name = student['first_name']
        if is_male[name]:
            count_boys += 1
        else:
            count_girls += 1
    print('В классе {} {} девочки и {} мальчика'.format(class_number['class'], count_girls, count_boys))


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print('\n\n')
# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
max_boys = 0
max_girls = 0

for class_number in school:
    count_boys = 0
    count_girls = 0
    for student in class_number['students']:
        name = student['first_name']
        if is_male[name]:
            count_boys += 1
        else:
            count_girls += 1
    if count_boys > max_boys:
        max_boys = count_boys
        max_class_boys = class_number['class']
    if count_girls > max_girls:
        max_girls = count_girls
        max_class_girls = class_number['class']

print(f'Больше всего мальчиков в классе {max_class_boys}')
print(f'Больше всего девочек в классе {max_class_girls}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a