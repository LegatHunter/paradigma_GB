# Урок 1. Императивное и декларативное программирование на практике
# Обязательные задачи:

# Императивное программирование:

# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.

# def SumNumbers(number):
#     summ = 0
#     i = 1
#     while i <= number:
#         i += 1
#         if i % 2 == 0:
#             summ += i
#     return summ
#
# numbrr = int(input("Введите число: "))
# print(SumNumbers(numbrr))



# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.

# def MinNum(numbers):
#     even_numbers = []
#     minNum = numbers[0]
#     for num in numbers:
#         if num < minNum:
#             minNum = num
#     return minNum
#
# numbers = [234, 44, 3, 4, 5, 6, 7, 8]
# print(MinNum(numbers))



# Декларативное программирование:

# Задача 3: Вычисление факториала числа. Напишите программу, которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.




# Задача 4: Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.
#
# Дополнительные сложные задачи (по желанию):
#
# Императивное программирование:
# Задача 5: Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном диапазоне от 1 до N.
# Задача 6: Упорядочивание списка. Напишите программу, которая сортирует список чисел в порядке возрастания с использованием пузырьковой сортировки или другого метода сортировки.
#
# Декларативное программирование:
# Задача 7: Поиск подстроки. Напишите программу, которая находит все вхождения заданной подстроки в строке с использованием встроенных функций.
# Задача 8: Вычисление суммы цифр числа. Напишите программу, которая вычисляет сумму всех цифр заданного числа, используя математические операции и деление нацело.