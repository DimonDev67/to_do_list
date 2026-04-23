# LIST COMPREHENSION
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# num = []
# for i in numbers:
#     if i % 2 == 0:
#         num.append(i**3)
# print(num)

# num = [i**3 for i in numbers if i % 2 == 0]
# print(num)


# DICT COMPREHENSION

# num = {
#    i: i**2 for i in range(10)
# }
# print(num)




# [ЧТО сделать   for КОГО   if УСЛОВИЕ]


# ОПЕРАТОР УПАКОВКИ И РАСПАКОВКИ
# num = [1, 2, 3, 4, 5]
# print(*num)

# num = [0, 1, 2, 3, 4]
# num2 = [5, 6, 7, 8, 9]
# result = [*num, *num2]
# print(result)

# num = [1, 2, 3]

# ДЕСТУКТУРИЗАЦИЯ
# a, b, c = num

# slovar = {
#     'x': 10
# }
# dictionary = {
#     'z': 9
# }
# result = {**slovar, **dictionary}
# print(result)

# zip() - УПАКОВЫВАЕТ СПИСКИ
# names = ['Vasya', 'Dima', 'Vova', 'Vanya', 'Yarik']
# salary = [2000, 999999999999999, 12345, 0.965765876, 0.00000000009999]
# rst = list(zip(names, salary))
# print(rst)


# a = [1, 2]
# b = [3, 4]
# c = [5, 6]
# result = [*a, *b, *c]
# print(result)

# names = ["Alice", "Bob"]
# ages = [25, 30]
# cities = ["Paris", "Berlin"]
# result = list(zip(names, ages, cities))
# print(result)


# def sum(*element):
#     return element
# print(sum())
# text = "hello world hello python world"
# split = text.split()
# mnozhestvo = set(split)
# print(split)
# print(mnozhestvo)

# cortesh = (1, 2, 3, 4, 5)
# mnozh = list(cortesh)
# print(mnozh)
# mnozh.append(6)
# print(mnozh)
# mosg = tuple(mnozh)
# print(mosg)

# a = [1, 2, 2, 3, 4, 4, 5]
# spetcialni_spisok = []
# for i in a:
#     if i not in spetcialni_spisok:
#         spetcialni_spisok.append(i)
# print(spetcialni_spisok) 

# t = (5, 10, 15, 20)
# b = 0
# for i in t:
#     b+=i
# print(b)


# lambda - анонимная(безымянная) функция в 1 строку
# def summa(a, b):
#     return a+b
# print(summa(12, 13))

# a = lambda a,b: a/b
# print(a(1, 5))


# users = [
#     {"name": "Иван", "age": 30},
#     {"name": "Анна", "age": 25},
#     {"name": "Петр", "age": 28}
# ]

# su = sorted(users, key=lambda r: r['age'], reverse=False)
# print(su)

# def odd(a):
#     if a % 2 == 0:
#         print('ЧИСЛО ЧЕТНОЕ')
#     else:
#         print("ЧИСЛО НЕЧЕТНОЕ")
# odd(1)


# a = lambda b: 'ЧЧ' if b % 2 == 0 else "НЧ"
# print(a(0))


# a = lambda b: b**2
# print(a(12))


# MAP AND FILTER - встроенные функции для обработки последоватеьностей(список, кортеж, множество)
# a = [1, 2, 3, 4, 5]
# b = set(map(lambda x: x**2, a))
# print(b)

# a = ['7', '4', '41', '99', '24']
# b = list(map())
# print(b)

# def a(x):
#     return x**3

# b = [1, 2, 3, 4, 5]
# c = list(map(a, b))
# print(c)


# filter
# a = [7, 51, 82, 9, 1, 87, 8, 26, 43, 94, 49, 27, 90, 5, 4]
# b = list(filter(lambda c: c % 2 == 0, a))
# print(b)
words = ["cat", "elephant", "dog", "tiger"]
a = list(filter(lambda i: len(i) >3, words))
print(a) 