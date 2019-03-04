 # Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
a = []
for i in students:
  if i not in a:
    a.append(i)
    print(f"{i['first_name']}: {students.count(i)}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# Пример вывода:
# Самое частое имя среди учеников: Маша
a = 0
b = []
for i in students:
  if students.count(i) > a:
    a = students.count(i)
    b = i
print(f"Самое частое имя среди учеников: {b['first_name']}")

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
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
a = 0
b = []
for i in school_students:
  for j in i:
    if i.count(j) > a:
      a = i.count(j)
      b = j
print(f"Самое частое имя среди учеников: {b['first_name']}")

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
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for i in school:
  man, woman = 0, 0
  for j in i['students']:
    if is_male[j['first_name']] == False:
      woman += 1
    else:
      man += 1
  print(f"В классе {i['class']} {woman} девочки и {man} мальчика.")


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
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
a,c = 0,0
b,d = [],[]
for i in school:
  man, woman = 0, 0
  for j in i['students']:
    if is_male[j['first_name']] == False:
      woman += 1
    else:
      man += 1
  i['man'] = man
  i['woman'] = woman
for i in school:
  if i['man'] > a:
    a = i['man']
    b = i['class']
  elif i['woman'] >c:
    c = i['woman']
    d = i['class']
print(f"Больше всего мальчиков в классе {b}")
print(f'Больше всего девочек в классе {d}')


