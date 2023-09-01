
# Задача: Вычисление факториала
# Напишите программу, которая запрашивает у пользователя число n и вычисляет факториал этого числа с использованием цикла.

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# n = int(input("Введите число: "))

# print(factorial(n))




# Функциональное программирование:
# Задача: Сумма квадратов четных чисел
# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов четных чисел в списке, используя функциональные конструкции

# def sum(numbers):
#     sum = 0
#     for num in numbers:
#         if num % 2 == 0:
#             sum += num**2
#     return sum


# n = [5, 6, 7, 4, 6]
# print(sum(n))
# Объектно-ориентированное программирование:
# Задача: Магазин и продукты
# Создайте классы Product и Store для моделирования магазина и продуктов. У магазина должны быть методы для добавления продуктов, отображения ассортимента и расчета общей стоимости покупки. Продукты могут иметь атрибуты, такие как название, цена и количество.

# class Product:
#     name = name
#     price = price
#     cout = count

# class Store:
#     def add_product(self):
#         product = []
#         product.append(product)
#     def get_product(self):
#         print()
#     def calculate(self, product):
#         total = 0
#         for product in 

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# class Store:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def display_products(self):
#         print("Ассортимент магазина:")
#         for product in self.products:
#             print(f"{product.name} - Цена: {product.price} руб, Количество: {product.quantity}")

#     def calculate_total(self, shopping_list):
#         total_cost = 0
#         for item in shopping_list:
#             for product in self.products:
#                 if item["name"] == product.name:
#                     total_cost += product.price * item["quantity"]
#                     break
#         return total_cost

# # Создание продуктов
# product1 = Product("Яблоко", 50, 10)
# product2 = Product("Молоко", 80, 5)
# product3 = Product("Хлеб", 30, 8)

# # Создание магазина и добавление продуктов
# store = Store()
# store.add_product(product1)
# store.add_product(product2)
# store.add_product(product3)

# # Отображение ассортимента магазина
# store.display_products()

# # Список покупок
# shopping_list = [
#     {"name": "Яблоко", "quantity": 3},
#     {"name": "Молоко", "quantity": 2},
#     {"name": "Хлеб", "quantity": 1}
# ]

# # Расчет общей стоимости покупки
# total_cost = store.calculate_total(shopping_list)
# print(f"Общая стоимость покупки: {total_cost} руб.")

# Решение 2

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def __str__(self):
#         return f"{self.name} - {self.price}$ ({self.quantity} pcs)"


# class Store:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def display_products(self):
#         if not self.products:
#             print("The store is empty.")
#         else:
#             print("Products available in the store:")
#             for product in self.products:
#                 print(product)

#     def calculate_total_price(self, shopping_cart):
#         total_price = 0
#         for item in shopping_cart:
#             for product in self.products:
#                 if item['name'] == product.name:
#                     if item['quantity'] <= product.quantity:
#                         total_price += item['quantity'] * product.price
#                         product.quantity -= item['quantity']
#                     else:
#                         print(f"Not enough {product.name} in stock.")
#         return total_price
# product1 = Product("Apple", 1.0, 10)
# product2 = Product("Banana", 0.5, 20)
# product3 = Product("Orange", 1.2, 15)
# store = Store()
# store.add_product(product1)
# store.add_product(product2)
# store.add_product(product3)
# store.display_products()
# shopping_cart = [
#     {'name': 'Apple', 'quantity': 5},
#     {'name': 'Banana', 'quantity': 10},
# ]
# # Рассчитываем общую стоимость покупки
# total_price = store.calculate_total_price(shopping_cart)
# print(f"Total price: {total_price}$")
# store.display_products()

# Функциональное программирование:
# Задача: Подсчет количества слов в строке
# Напишите функцию, которая принимает строку и возвращает количество слов в этой строке. Слова разделены пробелами.

# def cout_words(string):
#     words = string.split()
#     return len(words)
# string1 = input()
# wc = cout_words(string1)
# print(wc)

# Логическая парадигма

# Задача: Поиск числа в списке

# Условие: Дан список чисел. Напишите программу, которая проверяет, содержится ли заданное число в списке.

# def search(num, count):
#     if count in num:
#         return True
#     else:
#         return False

# numbers = [1, 2, 3, 4, 5, 6]
# count = int(input())

# if search(numbers, count):
#     print("Yes")
# else:
#     print("No")

# Напишите программу, которая сортирует список чисел методом сортировки слиянием.

# Сортировка слиянием - это эффективный алгоритм сортировки, который разбивает список на две половины, сортирует их отдельно, а затем объединяет в отсортированный список. Задача состоит в том, чтобы написать программу, которая будет сортировать список чисел методом сортировки слиянием.

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i]< right[j]:
#                 nums[k]=left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k] = right[j]
#             j+=1
#             k+=1

# a = [2, 4, 6, 1 ,8, 14, 546, 564, 2, 12, 0, 12, 45, 78]
# merge_sort(a)
# print(a)


# Реализовать секундомер на любом языке программирования
# в любой парадигме. Секундомер должен поддерживать
# следующий функционал:
# ○ Запуск
# ○ Пауза
# ○ Выход из паузы
# ○ Остановка

# import time

# class Stopwatch:
#     def __init__(self):
#         self.start_time = None
#         self.pause_time = None
#         self.paused = False

#     def start(self):
#         if not self.paused:
#             self.start_time = time.time()
#         else:
#             self.start_time += time.time() - self.pause_time
#             self.paused = False

#     def pause(self):
#         if not self.paused:
#             self.pause_time = time.time()
#             self.paused = True

#     def resume(self):
#         if self.paused:
#             self.start_time += time.time() - self.pause_time
#             self.paused = False

#     def stop(self):
#         elapsed_time = 0
#         if self.start_time is not None:
#             if not self.paused:
#                 elapsed_time = time.time() - self.start_time
#             else:
#                 elapsed_time = self.pause_time - self.start_time
#         return elapsed_time

# stopwatch = Stopwatch()

# print("Нажмите Enter для запуска секундомера...")
# input()

# stopwatch.start()
# print("Секундомер запущен. Нажмите Enter для паузы...")
# input()

# stopwatch.pause()
# print("Секундомер на паузе. Нажмите Enter для возобновления...")
# input()

# stopwatch.resume()
# print("Секундомер возобновлен. Нажмите Enter для остановки...")
# input()

# elapsed_time = stopwatch.stop()
# print("Секундомер остановлен.")
# print("Прошло времени:", elapsed_time, "секунд")



# ● Пусть у нас есть два массива длины n: один с предсказаниями нашей модели - Ŷ, а другой с истиной
# (правильными ответами) - Y. Тогда можно вычислить MSE по простой формуле.
# ● Ваша задача
# Реализовать процедуру для вычисления MSE на любом языке в любой парадигме. Программа получает
# на вход два вектора и возвращает число - оценку MSE для этих векторов.

# def calculate_mse(predictions, true_values):
#     if len(predictions) != len(true_values):
#         raise ValueError("The length of predictions and true_values must be the same.")
    
#     n = len(predictions)
#     mse = sum((predictions[i] - true_values[i])**2 for i in range(n)) / n
    
#     return mse

# # Пример использования
# predictions = [1, 2, 3, 4, 5]
# true_values = [1.5, 2.5, 3.5, 4.5, 5.5]

# mse = calculate_mse(predictions, true_values)
# print("MSE:", mse)