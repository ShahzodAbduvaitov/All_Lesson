#  # Переменные в Phyton
#
# name = 'Pasha'
# print(name)
#
# # Типы данных в Phyton(integer, float, string, boolean)
#
#
# print('Hello Albert')  # На экран выводится Hello Albert (тип данных string) важно запомнить что числа и все вводные данные находящиеся в ковычках будут string
#
# print(12) #integer - целые числа
#
# print(12.2)  #float - числа с остатком после .
#
# # Boolean это логический оператор
# # >  	больше
# # <	    меньше
# # >=	больше или равно
# # <=	меньше или равно
# # ==	равно
# # !=	не равно
# a = 100
# b = int(input('Введите любое целое число: '))
# if a > b:
#     print('True')
# else:
#     print('False')
#
#
#
# # Математичесмке операторы
# # + складывание
# # - вычитание
# # * умножение
# # / деление
# # ** возведение в степень 5 ** 2 = 25
# # % остаток от деления 5 % 2 = 1
# # // деление без остатка 5 // 2 = 2
#
# num1 = 5
# num2 = 4
# total1 = num1 + num2
# total2 = num1 - num2
# total3 = num1 * num2
# total4 = num1 / num2
# total5 = num1 ** num2
# total6 = num1 % num2
# total7 = num1 // num2
#
# print(total1,total2,total3,total4,total4,total5,total6,total7)
#
# # Так же можно работать не только с типом данных integer, float, но и с String
# x = 'hello'
# y = 2
# print(x*y)
# x = 'Phy'
# y = 'ton'
# print(x+y)
#
# # Функция input позволяет вывести на экран данные введеные пользователем
#
# print(input('Введите любое слово: '))
#
# #List, списки
# # List Slicing - вывести только определенную часть из списка, которую мы хотим видеть
# # p = [ ] Пустой список
# # p = [ 5 ] Список с одним элементом
# # p = [ 1, 4.12,'Hello', [ 1,'2','Name'] ] Список сразными элементами
#
# names = ['Ivan', 'Pavel', 'Jordan', 5]
# print(type(names))
# # Можно делать список в списке
# names = [1, 2, 3, 4, ['Hello', 3, '5']]
# print(type(names))
#
# # С помощью *len можно узнать количество элементов
#
# students = ['Shahzod', 'Manssur', 'Nikita']
# print(len(students))
#
# # У каждого элемента есть свой индекс через который к нему можно обратиться (начиная с 0 и до ...., если начинать с конца -1, -2, -3 ......
#
# students = ['Shahzod', 'Manssur', 'Nikita']
# print(students[0])
# print(students[-1])
# print(students[0][-1])
#
# # Так же можно брать от [x] и до [y] какого либо элемента [x:y] и так же [x:y:z] где z это промежуток
# list = [1, 2, 3, 4, 5, 'Sasha', 'Anna', 2.3]
# print(list[2:-2])
# print(list[0:-1:2])
#
# # .append добавление элемента в конец списка, .insert(индекс, новый элемент) - добавить элемент в определенное место(индекс) .extend() - добавить несколько элементов в список
# list = [1, 2, 3, 4, 5, 'Sasha', 'Anna', 2.3]
# list.append('Malika')
# print(list)
# name = ['Abbos', 'Artur', 'Sasha', 'Shahzod']
# name.insert(4, 'Albert')
# print(name)
# names = ['Loki', 'Spiderman']
# names.extend(['Thor', 0, 23,'Tanos'])
# print(names)
#
# # Методы для удаления: .clear() - удалить все элементы списка, .pop() - удаляет последний элемент списка или можно передать индекс элемента который хотим удалить,.remove(элемент) - удаляет элемент который мы передадим
# students = ['Abbos', 'Artur', 'Sasha', 'Shahzod', 'Anna', 'Artem', 'Malika', 'Doni']
# students.pop()
# print(students)
# students.pop(1)
# print(students)
# students.remove('Anna')
# print(students)
# students.clear()
# print(students)
#
# # Так же есть методы для изменения, .sort - сортирует по алфавиту, .reverse - переварачивает список с -1 и до 0
# Class = ['Abbos', 'Artur', 'Sasha', 'Shahzod', 'Anna', 'Artem', 'Malika', 'Doni']
# Class[4] = 'Ekaterina'
# print(Class)
# Class.sort()
# print(Class)
# Class.reverse()
# print(Class)
#
# # Картежи (Tuples)
# # Tuples slicing такой же как и List slicing
# my = (1, 'Hello', [1, '2', 'Name'], (1, 4.12))  # Кортеж со множеством элементов
# my = 2, 3, 'Hello'  # тоже кортеж
# my = ('Name')  # Кортеж с одним элементом
#
# # Примечания
# # toys = ('Мишка', 'Мячик', 'Робот', 'машинка')
# # toys2 = list(toys)
# # print(toys2)  # ['Мячик', 'Робот', 'машинка']
# # print(type(toys))  # <class 'tuple'>
# # toys = ['Мишка', 'Мячик', 'Робот', 'машинка']
# # toys2 = tuple(toys)
# # print(toys2)  # ('Мячик', 'Робот', 'машинка')
# # print(type(toys2))  # <class 'tuple'>
#
# #Для проверки на наличие элемента в списке или в кортеже используются условные операторы (if, elif, else) и ключевое слово in
# Class = ('Abbos', 'Artur', 'Sasha', 'Shahzod', 'Anna', 'Artem', 'Malika', 'Doni')
# if 'Anna' in Class:
#     print('Yes, this name in class')
# else:
#     print('Sorry, this name delete')
#
# # Цыклы for и While
# name = 'Shahzod'
# for i in name:
#     print(name)
#
# list = [1, 2, 3, 'Sasha']
# for i in list:
#     print(i)
#
# # Функция range
# name = ['Shahzod', 'Pasha', 'Nikita', 'Artur']
# for i in range(1,5):
#     if 'Shahzod' in name:
#         print('В списке')
#     else:
#         print('Нету')
#
# #While
# name = ['Shahzod', 'Pasha', 'Nikita', 'Artur']
#
# # while True:
# #     new_name = input('Введите новое имя: ')
# #     name.append(new_name)
# #     print(name)
#
# #List comprehension
# a = 'Shahzod'
# b = [c for c in name]
# print(b)
#
# nums = [i for i in range(0, 100)]
# print(nums)
#
# # Словари
# slov = {'name': 'Malika', 'job': 'ticher'}
# print(slov['name'])
#
# a = input('Введите имя: ')
# c = {'name': a, 'job': 'ticher'}
# print(c['name'])
#
# # Методы словарей , .values() - выдаст все значения всех ключей .keys() - выдаст все ключи словаря, .items() - выдаст оба значения словаря
# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# print(instructor.values())
# print(instructor.keys())
# print(instructor.items())
#
# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# if 'age' == 23 in instructor:
#     print('Yes')
# else:
#     print('NO')
#
# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
# if 21 in instructor.values():#.keys or .items
#     print('Yes')
# else:
#     print('NO')
#
# users = {}
# users['name'] ='Shahzod'
# users['job'] = input('Введите свою должность: ')
# print(users['name'], users['job'])
#
# #Добавление новых ключ-значений
# songs = {}
# songs['singer'] = 'MIYAGI'
# songs['name'] = 'Freeman'
# print(songs)
#
# #Методы для удаления
# my_dict = {'singer': 'Eminem', 'song': 'Gadzilla'}   # Очищает весь словарь
# my_dict.clear()
# print(my_dict)
#
#
# users = {'Albert': 22, 'Shahzod': 20, 'Malika': 25}   # Удаляет любую пару
# users.popitem()
# print(users)
#
# print({}.fromkeys('Shahzod', 22))   # Создает словарь (ключь, значение)
# print({}.fromkeys('song','Godzilla'))
#
# users = {'Albert': 22, 'Shahzod': 20, 'Malika': 25}  # Выдает значение переданного ключа
# print(users.get('Malika'))
#
# my1 = input('Введите имя: ')
# my2 = {'name': my1, 'age': 23}
# my2.pop('age')  # Удаляет выбранный ключ с его значением
# print(my2)
#
# my = dict(name='Shahzod', job='programmist', age=23)
# my2 = my.copy()  # копирует данные с переменной и вставляет их в другую переменную
# print(my2)
#
# # Сеты (sets) - набор неповторяющихся значений, если есть повторяющиеся элементы в списке, сеты возвращают только одно (сортируют). Сеты не имеют индексов - мы не сможем взять доступ к определенным элементам names = {'Names', 1, 2, 3, 4, 5} print(names[0])
# nums = {1, 2, 3, 3, 4, 4, 5}
# nums2 = set({'Hello', 'Hello', 'myname', 2, 2, 0})
# print(nums)
# print(nums2)
#
# # Мы можем применить set() к картежам, листам и убрать из них повторяющиеся значения
# nums = (1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9)
# nums2 = set(nums)
# print(nums2)
#
# list = [1, 2, 3, 4, 5, 'Sasha', 'Anna', 'Anna',  2.3]
# list2 = set(list)
# print(list2)

# # Циклы for в словарях
# users = dict(name='Shahzod', age=25, job='developer')
# for i in users.keys():  # Выводит ключи словаря
#     print(i)
#
# users = dict(name='Shahzod', age=25, job='developer')
# for i in users.values():  # Выводит значение словаря
#     print(i)
#
# users = dict(name='Shahzod', age=25, job='developer')
# for i in users.items():  # Выводит все значения словаря
#     print(i)

# Функции (functions) - процесс выполнения какого либо действия (множество строк кода объединенные в один красивый шаблон), которое мы можем вызвать в любом месте нашего кода

# def nums():  # def - с помощью нее мы можем поместить какой-либо кусок кода в переменную, а после вызвать эту переменную в нужном нам месте
#     num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     print(num)
# nums()
#
# def calculator():
#     print(56*4)
# calculator()

# def num(x, y, z):
#     return x + y + z  # def spam1(**kwargs):
# for k,v in kwargs:
# return k, v
# print(spam1(name= 'my1'
# , age= 23)return - сохраняет и возвращяет значение
# result = num(1, 2 ,3)
# print(result)

# Параметры функции Параметров функций может быть одно, множество или вообще может не быть мы перечисляем их через запятую Параметры могут быть обязательными или необязательными
# def primer(a, b):
#     print(a+b)
# primer(7,8)
#
# def primer2(a, b, c=7):  # с=7 здесь не обязательный параметр
#     print(a+b*c)
# primer2(5, 4)  # Если не задавать парамет "c", то он по умолчанию возмет как с=7
# primer2(5, 4, 2)  # Но так же можно задать параметр, который хотим

# Запомнить
# def spam2(параметры):
#     print(a+b)
# spam2(аргументы)
#
# def spammer(*args):  # Зададет любое количество аргументов
#     for a in args:
#         print(a)
# spammer(1, 2, 3, 1, 2, 3, '4', 'Hello')

# def a1(*args):
#     if 'Shahzod' in args:
#         print('Есть')
#     else:
#         print('Нету')
# a1(1, 2, 3, 'Shahzod')

# **kwargs - задавать любое количество аргументов (ключ: значение)
# def peremennaya(**kwargs):
#     return kwargs
#
# print(peremennaya(name='Sh', age='23'))

# Lambda функции - это специальный метод создания функций в Python в одну строку
# a = lambda x: x**2
# print(a(12))

# map() - встроенная функция в Python, которая принимает 2 аргумента (функция(чаще всего lambda), итерируемый объект(str, list, tuple, dict) функция передаваемая в аргумент будет выполняться для каждого элемента итерируемого объект

# x = [1, 2, 3, 4]
# y = map(lambda d: d*2, x)
# print(list(y))

# filter() - встроенная функция в Python, которая принимает 2 аргумента (функция(чаще всего lambda), итерируемый объект(str, list, tuple, dict) Возвращает те значения, которые соответствуют условию функция передаваемая в аргумент будет выполняться для каждого элемента итерируемого объекта

# x = [1, 2, 3, '4']
# a = filter(lambda d: d*2 == 4, x)
# print(list(a))

# l = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x%2 == 0, l))
# print(a)

# x = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
# y = list(filter(lambda a: a>0, x))
# print(list(y))


# def decrement_list(nums):
#     o = list(map(lambda x: x-2, nums))
#     return o
# print(decrement_list([1,2,3,4,5]))

# Классы и объекты ООП - это метод в программировании который позволяет
# смоделировать(создавать) что-либо или процессы из жизни
# Они создаются с использованием классов или объектов
# ООП (объектно-ориентированное
# программирование)
# Класс - это план для создания объектов(конструктор
# объектов)
# Классы могут содержать свои методы(функции) и аттрибуты

# class Car:
#     max_speed = 300
#     color = "red"
#     car_name = 'Bugatti'
#
# class Home:
#     def __init__(self, person, quantity_room, size):
#         self.person = person
#         self.quantity = quantity_room
#         self.size = size
#
# first_home = Home('12 человек,', 'пять комнат,', '42 квадратных метра' )
# print(first_home.person, first_home.quantity, first_home.size)
#
#
# class Comment:
#     def __init__(self, user_name, text, likes=500):
#         self.user_name = user_name
#         self.text = text
#         self.likes = likes
#
# first_comm = Comment('Shahzod', 'WOOOOW')
# second_comm = Comment('Malika', 'not BAD', 400)
#
# print(first_comm.user_name, second_comm.text, second_comm.likes)

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Машина остановилась на светофоре')
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# tt = Car('AUDI', 'yelow', 2022)
# tt.change_color('Black')
#
# print(tt.model, tt.color, tt.year)

# class BankAccaunt:
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, money):
#         self.balance += money
#
#
#     def cash(self, money):
#         self.balance -= money
#
#
#     def show_balance(self):
#         return self.balance
#
# name = input('Добро пожаловать, введите свое имя: ')
# client1 = BankAccaunt(name)
# while True:
#
#     choice = int(input('1 - Депозит\n2 - Снять деньги\n3 - Посмотреть баланс: '))
#
#     if choice == 1:
#         amount = int(input('Сколько денег вы хотите добавить в депозит? '))
#         client1.deposit(amount)
#
#     elif choice == 2:
#         amount = int(input('Сколько денег вы хотите снять? '))
#         client1.cash(amount)
#
#     elif choice == 3:
#         print(client1.show_balance())
#
#     else:
#         print('Выберите пункт из меню!')

# class User:
#     def __init__(self, name, mail, age, number):
#         self.name = name
#         self.mail = mail
#         self.age = age
#         self.number = number
#
#     def change_username(self, user_name):
#         self.name = user_name
#
#     def change_number(self, num):
#         self.number = num
#
#     def change_mail(self, new_mail):
#         self.mail = new_mail
#
#     def change_age(self, new_age):
#         self.age = new_age
#
# name = input('Добро пожаловать, введите свое имя: ')
# mail = input('Введи свою почту: ')
# age = int(input('Введите свой возраст: '))
# number = input('Введите свой номер: ')
#
# user1 = User(name, mail, age, number )
# while True:
#     menu = int(input('1 - Изменить имя:\n2 - Изменить номер:\n3 - Изменить почту:\n4 - Изменить возраст:\n5 - Посмотреть данные:  '))
#     if menu == 1:
#         change_name = input('Введите новое имя: ')
#         user1.change_username(change_name)
#
#     elif menu == 2:
#         num = input('Введите новый  номер телефона: ')
#         user1.change_number(num)
#
#     elif menu == 3:
#         mail = input('Введите новую почту: ')
#         user1.change_mail(mail)
#
#     elif menu == 4:
#        age = int(input('Введите свой возраст: '))
#        user1.change_age(age)
#
#     elif menu == 5:
#         print(user1.name, user1.number, user1.mail, user1.age)
#
#     else:
#         print('Выберите пункт из меню')


#
#
#
#
#
#
#
#
#
#
#
#







#
#
#
#
#
#
#
#
#
#
#
#
#
