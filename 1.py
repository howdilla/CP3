# Создаём переменную name с именем студента, переменную surname с фамилией студента и переменную date_of_birth с годом рождения.
name = input('Введите имя студента:')
surname = input('Введите фамилию студента:')
date_of_birth = int(input('Введите год рождения студента:'))

# Выводим значение name, surname и date_of_birth с _ между именем, фамилией и годом.
print(name, surname, date_of_birth, sep="_")

# Меняем содержимое переменных name и surname местами с использование новой переменной(x).
x = name
name = surname
surname = x

# К дате рождения прибавляем 60.
date_of_birth += 60

# Cнова выводим name, surname, и date_of_birth.
print(name, surname, date_of_birth)
